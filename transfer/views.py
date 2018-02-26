from django.shortcuts import render

# Create your views here.

from django.db.migrations import questioner
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, request
from .models import Transfer, Savings
from django.template import loader
from django.urls import reverse
from .transfer_form import TransferForm
from django.views.generic.base import TemplateView
from savings.views import confirmTransfer
import django.contrib.sessions.backends.signed_cookies


# Create your views here.


class ConfirmRedirect( TemplateView ):
    template_name = 'transfer/confirm/index.html'

    def get_context_data(self, **kwargs):
        context = super( ConfirmRedirect, self ).get_context_data( **kwargs )
        context["username"] = "This is a useless page"
        return context


class SavingsRedirect( TemplateView ):
    template_name = 'savings/index.html'

    def get_context_data(self, **kwargs):
        context = super( SavingsRedirect, self ).get_context_data( **kwargs )
        userame = self.request.session['userAccNo']
        context["username"] = "charles"
        return context


def index(request):
    # latest_question_list = Savings.objects.order_by('-pub_date')[:5]

    username = Savings.objects.get( id__exact=1 )

    form = TransferForm()
    context = {
        'form': form, 'username': username
    }
    # return HttpResponseRedirect( reverse( 'transfer:confirm' ) )
    return render( request, 'transfer/index.html', context )


# return HttpResponseRedirect('/transfer/confirm/index.html', {'username', username})


def formHandler(request, username):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TransferForm( request.POST )
        # check whether it's valid:
        # process the data in form.cleaned_data as required

        if form.is_valid():
            AccName = form.cleaned_data['userAccName']
            AccNo = form.cleaned_data['userAccNo']
            AccAmount = form.cleaned_data['userAccAmount']
            AccPasswd = form.cleaned_data['userAccPasswd']
            recptAccNo = form.cleaned_data['recptAccNo']
            # redirect to a new URL:

            try:

                DBobj = get_object_or_404( Savings, userAccNo__exact=AccNo )
                recptobj = get_object_or_404( Savings, userAccNo__exact=recptAccNo )

                AccBal = DBobj.userAccBal
                receptAccBal = recptobj.userAccBal

                request.session['username'] = DBobj.userAccName
                request.session['userbal'] = DBobj.userAccBal
                request.session['userAccNo'] = DBobj.userAccNo

            except (KeyError, DBobj.DoesNotExist):
                return HttpResponseRedirect( 'index.html',
                                             {'DBobj': DBobj, 'message': "You did not select a fill any field"} )
            else:

                AccBal = AccBal - AccAmount
                receptAccBal += AccAmount
                # MyModel.objects.get( name=name ).update( field=value )
                Savings.objects.filter( userAccNo__exact=AccNo ).update( userAccBal=AccBal )
                Savings.objects.filter( userAccNo__exact=recptAccNo ).update( userAccBal=receptAccBal )

                ########################################################################

                activity="transfered'+AccAmount+' to '+recptAccNo'"
                a=DBobj.userAccName

                ########################################################################

                request.session['recpt_uname'] = recptobj.userAccName
                request.session['sender_uname'] = DBobj.userAccName
                request.session['sender_amnt_bal'] = AccBal
                request.session['recpt_amnt_bal'] = receptAccBal
                request.session['amnt_sent'] = AccAmount
                request.session['sender_acc_no'] = AccNo

                return HttpResponseRedirect( reverse( 'transfer:confirm', ), {'username': DBobj},{'message':message} )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TransferForm()
        return HttpResponseRedirect( render( request, 'transfer/index.html', {'form': form} ) )


