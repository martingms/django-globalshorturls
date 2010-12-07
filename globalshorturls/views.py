# encoding: utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from globalshorturls.models import Shorturl, ShorturlForm
from globalshorturls.baseconv import base62

@login_required
def index(request):
    '''
        View that gives you a prompt for shortening an URL, and shows the users shortened urls.
    '''
    user = request.user
    user_shorturls = Shorturl.objects.filter(creator=user)

    if request.method == "POST":
         shorturlform = ShorturlForm(request.POST)
         if shorturlform.is_valid():
            shorturl = Shorturl(url=shorturlform.cleaned_data['url'], creator = user)
            shorturl.save()


    shorturlform = ShorturlForm()

    return render_to_response('globalshorturls/index.html',
                         {'usershorturls'  : user_shorturls,
                          'shorturlform'   : shorturlform,
                          # User is not used in the example index.html template, but might be useful
                          'user'           : user, },
                          context_instance=RequestContext(request))

def redirect(request, shorturl):
    '''
        Redirects a yourdomain.com/XYZ shorturl to the full url
    '''
    try:
        url = Shorturl.objects.get(shorturl=shorturl)
        #TODO find a better way to save stats, this slows down the redirect a little bit
        url.counter += 1
        url.save()
        return HttpResponseRedirect(url.url)
    except:
        raise Http404

@login_required
def delete_shorturl(request, url_id):
    '''
        Deletes the shorturl with id url_id
    '''
    shorturl = get_object_or_404(Shorturl, pk=url_id)

    if shorturl.creator == request.user:
        shorturl.delete()
        # You might want some kind of message saying success here
        return HttpResponseRedirect(reverse('globalshorturls.index'))

    # You might want some kind of message saying you can't delete other peoples urls here
    return HttpResponseRedirect(reverse('globalshorturls.index'))