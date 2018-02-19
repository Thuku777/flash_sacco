from django.shortcuts import render
from django.db.migrations import questioner
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.contrib.sessions.backends.signed_cookies import SessionStore

import django.contrib.sessions.backends.signed_cookies
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,request
from django.template import loader
from django.urls import reverse
from django.views.generic.base import TemplateView
from user.loan_form import LoanForm
from django.views.generic.edit import UpdateView
from transfer.models import Savings
import django.contrib.sessions.backends.signed_cookies
# Create your views here.
# Create your views here.




class UserPage(TemplateView):
    template_name = 'user/index.html'

    def get_context_data(self, **kwargs):
        context=super(UserPage, self).get_context_data(**kwargs)
        context["username"]="This is a useless page"

        return context




class Member(TemplateView):
    template_name = 'user/members.html'

    def get_context_data(self , **kwargs):
        context=super(Member, self).get_context_data(**kwargs)
        uname=self.request.session['uname']="charles mwaniki"
        context['uname']=uname
        return context


class History(TemplateView):
    template_name = 'user/history.html'

    def get_context_data(self , **kwargs):
        context=super(History, self).get_context_data(**kwargs)
        uname=self.request.session['uname']="charles mwaniki"
        context['uname']=uname
        return context


class Loans(TemplateView):
    template_name = 'user/loans.html'
    form_class = LoanForm

    def get_context_data(self , **kwargs):
        context=super(Loans, self).get_context_data(**kwargs)
        uname=self.request.session['uname']="charles mwaniki"
        context['form']=LoanForm
        return context


def profileUpdate(UpdateView):
    model = Savings
    fields = ['curPassword', 'newPassword', 'newPassword2']
    template_name_suffix = '_update.html'
