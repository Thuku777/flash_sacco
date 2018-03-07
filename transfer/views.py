from django.shortcuts import render

# Create your views here.

from django.db.migrations import questioner
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, request
#from savings.models import Savings,Shares
from django.template import loader
from django.urls import reverse
from .transfer_form import TransferForm, SharesForm
from django.views.generic.base import TemplateView
#from transfer.models import TransferHistory
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
                TransferHistory.objects.filter( userAccNo__exact=1234 ).update( userAccName='Women', userAccNo=1234,
                accType='personal', groupAccNo=1234,userAccBal=123, amount=122, shares=0,activity='transfer',userAccBankBranch='nyc', activityType='transfer', status='works' )

                ########################################################################

                request.session['recpt_uname'] = recptobj.userAccName
                request.session['sender_uname'] = DBobj.userAccName
                request.session['sender_amnt_bal'] = AccBal
                request.session['recpt_amnt_bal'] = receptAccBal
                request.session['amnt_sent'] = AccAmount
                request.session['sender_acc_no'] = AccNo
                message="Mmmmhhh... Transfer was successful"
                return HttpResponseRedirect( reverse( 'transfer:confirm', ), {'username': DBobj},{'message':message} )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TransferForm()
        return HttpResponseRedirect( render( request, 'transfer/index.html', {'form': form} ) )


def sharesIndex(request):
    # latest_question_list = Savings.objects.order_by('-pub_date')[:5]

    username = Shares.objects.get( id__exact=1 )

    form = SharesForm()
    context = {
        'form': form, 'username': username
    }
    # return HttpResponseRedirect( reverse( 'transfer:confirm' ) )
    return render( request, 'transfer/shares.html', context )



def sharesHandler(request):
    if request.method == 'POST':
        form = SharesForm( request.POST )
        if form.is_valid():
            senderAccNo = form.cleaned_data['senderAccNo']
            recpAccNo = form.cleaned_data['recpAccNo']
            amount = form.cleaned_data['amount']
            # redirect to a new URL:
            try:

                DBobj = get_object_or_404( Shares, userAccNo__exact=senderAccNo )
                recptobj = get_object_or_404( Shares, userAccNo__exact=recpAccNo )

                AccBal = DBobj.num_of_shares
                receptAccBal = recptobj.num_of_shares

                request.session['username'] = DBobj.userAccNo
                request.session['AccBal'] = AccBal
                request.session['username'] = recptobj.userAccNo
                request.session['receptAccBal'] = receptAccBal

            except (KeyError, DBobj.DoesNotExist):
                return HttpResponseRedirect( 'shares.html',
                                             {'DBobj': DBobj, 'message': "You did not select a fill any field"} )
            else:
                message = "Mmmmhhh... Transfer was successful"
                return HttpResponseRedirect( reverse( 'transfer:confirm', ), {'username': DBobj}, {'message': message} )

        # if a GET (or any other method) we'll create a blank form
    else:
        form = SharesForm()
        ###################################Replace with session
        username = Shares.objects.get( id__exact=1 )
        ###################################
        return HttpResponseRedirect( reverse('transfer:shares', ), {'username': username})
