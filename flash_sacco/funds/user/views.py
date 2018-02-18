from django.shortcuts import render
from django.db.migrations import questioner
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib.sessions.backends.signed_cookies import SessionStore

import django.contrib.sessions.backends.signed_cookies
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,request
from django.template import loader
from django.urls import reverse
from django.views.generic.base import TemplateView

import django.contrib.sessions.backends.signed_cookies

# Create your views here.
# Create your views here.



class UserPage(TemplateView):
    template_name = 'user/index.html'

    def get_context_data(self, request, **kwargs):
        context=super(UserPage, self).get_context_data(**kwargs)
        context["username"]="This is a useless page"
            
        return context


class Profile(TemplateView):
    template_name = 'user/profile.html'

    def get_context_data(self , **kwargs):
        context=super(Profile, self).get_context_data(**kwargs)
        uname=self.request.GET
        #context["uname"] = self.request.GET.get( 'uname', '' )
        context['uname']=self.request.session['uname']
        return context



