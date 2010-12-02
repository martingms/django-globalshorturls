# encoding: utf-8
#FIXME all imports might not be in use
from django.shortcuts import render_to_response, get_object_or_404
from django import forms
from django.http import HttpResponseRedirect, Http404
from django.template import Context, loader, RequestContext
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
 	        shorturl.shorturl = base62.from_decimal(shorturl.id)
 	        shorturl.save()
 	        
    shorturlform = ShorturlForm()

    return render_to_response('globalshorturls/index.html',
                         {'usershorturls'  : user_shorturls,
                          'shorturlform'   : shorturlform,
                          'user'           : user, },
                          context_instance=RequestContext(request))
                          
def redirect(request, shorturl):
    '''
        Redirects a yourdomain.com/XYZ shorturl to the full url
    '''
    try:
        url = Shorturl.objects.get(shorturl=shorturl)
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
        return HttpResponseRedirect(reverse('ukeshorturls.index'))
 
    return HttpResponseRedirect(reverse('ukeshorturls.index'))