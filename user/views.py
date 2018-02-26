from django.shortcuts import render
from django.db.migrations import questioner
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.contrib.sessions.backends.signed_cookies import SessionStore

import django.contrib.sessions.backends.signed_cookies
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, request
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from user.loan_form import LoanForm, ProfileUpdateForm, PinUpdateForm, RegisterForm, RegisterGroupForm
from django.views.generic.edit import UpdateView
from savings.models import Savings
from user.models import User
from transfer.models import TransferHistory

import django.contrib.sessions.backends.signed_cookies


# Create your views here.
# Create your views here.


class Register( FormView ):
    template_name = 'user/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy( 'user:register' )


class RegisterGroup( FormView ):
    template_name = 'user/register.html'
    form_class = RegisterGroupForm
    success_url = reverse_lazy( 'user:register' )


class UserPage( TemplateView ):
    template_name = 'user/index.html'

    def get_context_data(self, **kwargs):
        context = super( UserPage, self ).get_context_data( **kwargs )
        ###########################################################
        uid = self.request.session['id'] = 1
        self.DBobj = get_object_or_404( User, pk__iexact=uid )
        ##########################################################
        context["DBobj"] = self.DBobj

        return context


class Update( UpdateView ):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'user/settings.html'
    # fields = ['firstName','lastName']

    success_url = reverse_lazy( 'user:profileupdate' )

    def get_object(self):
        # self.user = get_object_or_404( User, pk__iexact=self.args[0] )
        # self.user = get_object_or_404( User, pk__iexact=self.kwargs.get('pk', None) )
        self.user = get_object_or_404( User, pk__iexact=self.kwargs['slug'] )
        return self.user
        # return User.objects.filter( id=self.user )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super( Update, self ).get_context_data( **kwargs )
        # Add in the publisher
        context['DBobj'] = self.user
        # context['DBobj'] = User.objects.get( pk=1 )
        context['pinform'] = PinUpdateForm
        return context

    def pinUpdate(request, id):
        if request.method == 'POST':
            form = PinUpdateForm( request.POST )
            if form.is_valid():
                curContact = form.cleaned_data['contact']
                curContact_cp1 = form.cleaned_data['contact_cp1']
                curContact_cp2 = form.cleaned_data['contact_cp2']
                try:
                    DBobj = get_object_or_404( User, pk__exact=id )
                    pin = DBobj.contact

                except (KeyError, DBobj.DoesNotExist):
                    return HttpResponseRedirect( 'index.html',
                                                 {'DBobj': DBobj} )

                else:
                    if curContact == pin:

                        if curContact_cp1 == curContact_cp2:
                            User.objects.filter( pk__exact=id ).update( contact=curContact_cp2 )
                            message = 'Pin has been changed successfully'
                            return HttpResponseRedirect( reverse( 'user:profileupdate', args=[id] ),
                                                         {'form': form, 'message': message} )
                        else:
                            message = 'The two pins do not match. Try again.'
                            return HttpResponseRedirect( reverse( 'user:profileupdate', args=[id] ),
                                                         {'form': form, 'error': message} )

                    else:
                        message = 'You have entered a wrong pin.'
                        return HttpResponseRedirect( reverse( 'user:profileupdate', args=[id] ),
                                                     {'form': form, 'error': message, } )

            else:
                form = PinUpdateForm()
                return HttpResponseRedirect( render( request, 'user:profileupdate', {'form': form} ) )


class Member( TemplateView ):
    template_name = 'user/members.html'

    def get_context_data(self, **kwargs):
        context = super( Member, self ).get_context_data( **kwargs )
        # uname=self.request.session['uname']="charles mwaniki"
        ###########################################################
        DBobj = get_object_or_404( User, pk=1 )
        userSet = User.objects.all()
        ###########################################################
        context['DBobj'] = DBobj
        context['userSet']=userSet
        return context


class History( TemplateView ):
    template_name = 'user/history.html'

    def get_context_data(self, **kwargs):
        context = super( History, self ).get_context_data( **kwargs )
        # uname=self.request.session['uname']="charles mwaniki"
        ###########################################################
        DBobj = get_object_or_404( User, pk=1 )
        historySet = TransferHistory.objects.all()
        ###########################################################
        context['DBobj'] = DBobj
        context['userSet'] = historySet

        return context


class Loans( TemplateView ):
    template_name = 'user/loans.html'
    form_class = LoanForm

    def get_context_data(self, **kwargs):
        context = super( Loans, self ).get_context_data( **kwargs )
        # uname=self.request.session['uname']="charles mwaniki"
        ###########################################################
        DBobj = get_object_or_404( User, pk=1 )
        ###########################################################
        context['form'] = LoanForm
        context['DBobj'] = DBobj
        return context
