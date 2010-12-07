from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.conf import settings

from globalshorturls.baseconv import base62

class Shorturl(models.Model):
    """
        Shorturl model
    """
    url = models.CharField(max_length=200)
    shorturl = models.CharField(max_length=200)
    creator = models.ForeignKey(User, verbose_name='creator', null = True)
    counter = models.IntegerField(default = 0, editable = True)

    creator.compact_filter = True

    def full_shorturl(self):
        return settings['SHORT_URL_PREFIX'] + shorturl

    def __unicode__(self):
        return self.url

    def save(self):
        super(Shorturl, self).save()
        if not self.shorturl:
            self.shorturl = base62.from_decimal(self.pk)
            self.save()

class ShorturlForm(ModelForm):
    class Meta:
        model = Shorturl
        fields = ('url',)

    def clean_url(self):
        url = self.cleaned_data['url']
        if url.startswith('http'):
            return url
        else:
            return 'http://'+url