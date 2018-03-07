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

import savings
from user.loan_form import LoanForm, ProfileUpdateForm, PinUpdateForm, RegisterForm, RegisterGroupForm,SharesForm
from django.views.generic.edit import UpdateView
from savings.models import Savings, Shares
from user.models import User, Group
#from transfer.models import TransferHistory

import django.contrib.sessions.backends.signed_cookies


# Create your views here.
# Create your views here.

class Register(FormView):
    template_name = 'user/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('user:register')


def buySharesHandler(request):

    if request.method == 'POST':
        form = SharesForm(request.POST)
        if form.is_valid():
            numofshares = form.cleaned_data['num_of_shares']
            try:
                DBobj = get_object_or_404(User, pk__exact=1)
                savingsobj=get_object_or_404(Savings, pk__exact=1)
            except (KeyError, DBobj.DoesNotExist):
                return HttpResponseRedirect('user/index.html',{'DBobj': DBobj})
            else:

                obj, created=Shares.objects.get_or_create(defaults={'savingsID_id':1,'num_of_shares':numofshares})
                if created == True:
                    shares= Shares.objects.get(savingsID_id=1)
                    curshares=shares+numofshares
                    shares.update(num_of_shares=curshares)

                message = 'Shares have bought successfully'
                context = {
                    'form': form,
                    'DBobj': DBobj,
                    'savingsobj': savingsobj,
                    'message': message
                }
                return HttpResponseRedirect(reverse('user:shares'), context)
    else:

        DBobj = get_object_or_404(User, pk__exact=1)
        form = SharesForm()
        sharesobj=Shares.objects.get(savingsID_id=1)

        context={
            'form': form,
            'DBobj':DBobj,
            'error':'erorr',
            'sharesobj':sharesobj

        }

        return render(request, 'user/shares.html',context)


class UserPage(TemplateView):
    template_name = 'user/index.html'

    def get_context_data(self, **kwargs):
        context = super( UserPage, self ).get_context_data( **kwargs )
        ###########################################################
        uid = self.request.session['id'] = 1
        self.DBobj = get_object_or_404( User, pk__iexact=uid )
        self.savingsobj = get_object_or_404(Savings, pk__iexact=uid)
        #self.sharesobj = get_object_or_404(Shares, pk__iexact=uid )
        ##########################################################
        context["DBobj"] = self.DBobj
        context['savingsobj']=self.savingsobj
        return context


class Update(UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'user/settings.html'
    #success_url = reverse_lazy('user:profileupdate')

    def get_object(self):
        # self.user = get_object_or_404( User, pk__iexact=self.args[0] )
        # self.user = get_object_or_404( User, pk__iexact=self.kwargs.get('pk', None) )
        self.user = get_object_or_404(User, pk__iexact=self.kwargs['slug'])
        return self.user
        # return User.objects.filter( id=self.user )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super( Update, self ).get_context_data(**kwargs)
        # Add in the publisher
        context['DBobj'] = self.user
        context['pinform'] = PinUpdateForm
        #self.pinUpdate(self.kwargs['slug'])
        return context

    def pinUpdate(request, id):
        if request.method == 'POST':
            form = PinUpdateForm( request.POST )
            if form.is_valid():
                curPin = form.cleaned_data['accountPin']
                curPin_cp1 = form.cleaned_data['accountPin_cp1']
                curPin_cp2 = form.cleaned_data['accountPin_cp2']
                try:
                    DBobj = get_object_or_404(User, pk__exact=id)
                    pin = DBobj.accountPin

                except (KeyError, DBobj.DoesNotExist):
                    return HttpResponseRedirect('settings.html', {'DBobj': DBobj})

                else:
                    if curPin == pin:
                        if curPin_cp1 == curPin_cp2:
                            User.objects.filter(pk__exact=id).update(contact=curPin_cp2)
                            message = 'Pin has been changed successfully'
                            return HttpResponseRedirect(reverse( 'user:profileupdate', args=[id]), {'form': form, 'message': message})
                        else:
                            message = 'The two pins do not match. Try again.'
                            return HttpResponseRedirect(reverse('user:profileupdate', args=[id]), {'form': form, 'error': message})
                    else:
                        message = 'You have entered a wrong pin.'
                        return HttpResponseRedirect( reverse('user:profileupdate', args=[id] ), {'form': form, 'error': message, })
            else:
                form = PinUpdateForm()
                return HttpResponseRedirect( render(request, 'user:profileupdate', {'form': form}))


class Member(TemplateView):
    template_name = 'user/members.html'

    def get_context_data(self, **kwargs):
        context = super( Member, self ).get_context_data( **kwargs )
        # uname=self.request.session['uname']="charles mwaniki"
        ###########################################################
        DBobj = get_object_or_404(User, pk=1)
        groupobj=get_object_or_404(Group, pk=1)
        userSet = User.objects.filter(group=groupobj.id)
        ###########################################################
        context['DBobj'] = DBobj
        context['userSet']=userSet
        return context


class History(TemplateView):
    template_name = 'user/history.html'

    def get_context_data(self, **kwargs):
        context = super( History, self ).get_context_data( **kwargs )
        # uname=self.request.session['uname']="charles mwaniki"
        ###########################################################
        DBobj = get_object_or_404( User, pk=1 )
        #TransferHistyor
        historySet = User.objects.all()
        ###########################################################
        context['DBobj'] = DBobj
        context['userSet'] = historySet

        return context


class Loans(TemplateView):
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
