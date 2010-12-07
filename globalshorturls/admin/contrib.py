# encoding: utf-8
from django.contrib.admin import site, ModelAdmin
from globalshorturls.models import Shorturl
from django.forms import ModelForm
from django.contrib.admin.filterspecs import FilterSpec, ChoicesFilterSpec
from django.utils.translation import ugettext as _
from django.utils.encoding import smart_unicode

# The list of objects can get extremely long. This method will
# override the filter-method for objects by specifying an extra
# attribute on the list of choices, thus only displaying a filter
# method to those objects actually existing in the database.
# Taken from: http://djangosnippets.org/snippets/1879/
class CustomChoiceFilterSpec(ChoicesFilterSpec):
    def __init__(self, f, request, params, model, model_admin):
        super(CustomChoiceFilterSpec, self).__init__(f, request, params, model, model_admin)
        self.lookup_kwarg = '%s__id__exact' % f.name
        self.lookup_val = request.GET.get(self.lookup_kwarg, None)
        self.objects = model.objects.all()

    def choices(self, cl):
        yield {'selected': self.lookup_val is None,
               'query_string': cl.get_query_string({}, [self.lookup_kwarg]),
               'display': _('All')}

        items = [i.creator for i in self.objects]

        items = list(set(items))

        for k in items:
            yield {'selected': smart_unicode(k) == self.lookup_val,
                    'query_string': cl.get_query_string({self.lookup_kwarg: k.id}),
                    'display': k}

FilterSpec.filter_specs.insert(0, (lambda f: getattr(f, 'compact_filter', False), CustomChoiceFilterSpec))

class ShorturlAdminForm(ModelForm):
    class Meta:
        model = Shorturl

    def clean_url(self):
        url = self.cleaned_data['url']
        if url.startswith('http'):
            return url
        else:
            return 'http://'+url

class ShorturlAdmin(ModelAdmin):

    # You might want to add has_change_permission and has_delete_permission here if anyone but staff can view admin

    form = ShorturlAdminForm
    fields = ('url',)
    search_fields = ['url']
    list_display = ('url', 'full_shorturl', 'creator', 'counter',)
    list_filter = ('creator',)

    def save_model(self, request, obj, form, change):
        if not obj.creator:
            obj.creator = request.user
        obj.save()

site.register(Shorturl, ShorturlAdmin)