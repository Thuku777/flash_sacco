from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, request

from savings.models import Savings, Shares
from user.models import User
from django.template import loader
from django.urls import reverse
from .transfer_form import TransferForm, SharesForm
from django.views.generic.base import TemplateView
from transfer.models import TransferHistory
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
    username = Savings.objects.get( id__exact=1 )
    DBobj=User.objects.get(id__exact=1)
    form = TransferForm()
    context = {
        'form': form, 'username': username, 'DBobj':DBobj
    }
    # return HttpResponseRedirect( reverse( 'transfer:confirm' ) )
    return render( request, 'transfer/index.html', context )


# return HttpResponseRedirect('/transfer/confirm/index.html', {'username', username})


def formHandler(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = TransferForm( request.POST )
        if form.is_valid():
            AccName = form.cleaned_data['userAccName']
            AccNo = form.cleaned_data['userAccNo']
            AccAmount = form.cleaned_data['userAccAmount']
            AccPasswd = form.cleaned_data['userAccPasswd']
            recptAccNo = form.cleaned_data['recptAccNo']

            try:
                senderobj = get_object_or_404( User, pk__iexact=1 )
                DBobj = get_object_or_404( Savings, userAccNo__exact=AccNo )
                recptobj = get_object_or_404( Savings, userAccNo__exact=recptAccNo )

                AccBal = DBobj.userAccBal
                receptAccBal = recptobj.userAccBal
                userpin=senderobj.accountPin
            except (KeyError, DBobj.DoesNotExist):
                return HttpResponseRedirect( 'transfer/index.html', {'username': senderobj, 'message': "You did not select a fill any field"} )

            if AccPasswd == userpin:
                if AccBal < AccAmount:

                    context={
                        'message': 'You dont have enough shares to transfer',
                        'username':senderobj
                    }
                    #return HttpResponseRedirect( reverse( 'transfer:index', ), {'username': DBobj},  {'message': message} )
                    return render( request, 'transfer/index.html', context )
                else:
                    AccBal = AccBal - AccAmount
                    receptAccBal += AccAmount
                    # MyModel.objects.get( name=name ).update( field=value )
                    Savings.objects.filter( userAccNo__exact=AccNo ).update( userAccBal=AccBal )
                    Savings.objects.filter( userAccNo__exact=recptAccNo ).update( userAccBal=receptAccBal )

                    ########################################################################
                    activitytxt = 'Transfered Ksh 1000 from Savings account to James (Account Number: 1234) today'
                    TransferHistory.objects.create( userAccName=DBobj.userID.firstName, userAccNo=DBobj.userAccNo,
                                                    accType=DBobj.acc_options, groupAccNo=DBobj.groupAccNo,
                                                    userAccBal=DBobj.userAccBal, amount=AccAmount, shares=0,
                                                    activity=activitytxt, userAccBankBranch='Nyeri',
                                                    activityType='transfer', status='Successful' )

                    TransferHistory.objects.create( userAccName=recptobj.userID.firstName, userAccNo=recptobj.userAccNo,
                                                    accType=recptobj.acc_options, groupAccNo=recptobj.groupAccNo,
                                                    userAccBal=recptobj.userAccBal, amount=AccAmount, shares=0,
                                                    activity=activitytxt, userAccBankBranch='Nyeri',
                                                    activityType='transfer', status='Successful' )

                    #######################################################################
                    message = "Mmmmhhh... Transfer was successful"

                    context = {
                        'amount': AccAmount,
                        'recepient': recptobj.userID.firstName,
                        'sender': DBobj.userID.firstName,
                        'senderbal': recptobj.userAccBal,
                        'senderobj': DBobj,
                        'message': message,
                        'transfer': 'Money'
                    }

                    # return HttpResponseRedirect( reverse( 'transfer:confirm', ), context )
                    return render( request, 'transfer/confirm/index.html', context )
            else:

                form = TransferForm()
                context = {
                    'form': form,
                    'username': senderobj,
                    'error':'Wrong PIN bruh...'
                }
                # return HttpResponseRedirect( reverse('transfer:sharesHandler', ), context)
                return render( request, 'transfer/index.html', context )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TransferForm()
        DBobj = User.objects.get( id__exact=1 )
        senderobj = get_object_or_404( User, pk__iexact=1 )
        context={
            'form':form,
            'username':DBobj,
        }
        return render( request, 'transfer/index.html', context )
        #return HttpResponseRedirect( render( request, 'transfer/index.html', context ) )
        #return HttpResponseRedirect( reverse( 'transfer:index', ), context )


def sharesHandler(request):
    if request.method == 'POST':
        form = SharesForm( request.POST )
        if form.is_valid():
            senderAccNo = form.cleaned_data['senderAccNo']
            recpAccNo = form.cleaned_data['recpAccNo']
            amount = form.cleaned_data['amount']
            userAccPasswd=form.cleaned_data['userAccPasswd']
            # redirect to a new URL:
            try:
                senderobj = get_object_or_404(Savings, userAccNo__exact=senderAccNo )
                recptobj = get_object_or_404(Savings, userAccNo__exact=recpAccNo )
                sharesobjsender = get_object_or_404(Shares, savingsID_id=senderobj.id )
                sharesobjrecpnt = get_object_or_404( Shares, savingsID_id=recptobj.id )

            except (KeyError, senderobj.DoesNotExist):
                context={
                    'error':'User details dont exist',
                    'senderobj': senderobj,
                }

                return HttpResponseRedirect( reverse( 'transfer:sharesHandler', ),context)
            userpin= senderobj.userID.accountPin
            if userAccPasswd == userpin:

                senderbal = sharesobjsender.num_of_shares
                receptbal = sharesobjrecpnt.num_of_shares

                if senderbal < amount:
                    context={
                        'error' : 'You dont have enough shares to transfer',
                        'senderobj': senderobj,
                    }
                    #return HttpResponseRedirect( reverse( 'transfer:sharesHandler', ), {'senderobj': senderobj},    {'message': message} )
                    return render( request, 'transfer/shares.html', context )

                else:
                    newaccbal = senderbal - amount
                    newreceptAccBal = receptbal + amount

                    Shares.objects.filter( savingsID_id=senderobj.id ).update( num_of_shares=newaccbal )
                    Shares.objects.filter( savingsID_id=recptobj.id ).update( num_of_shares=newreceptAccBal )

                    ########################################################################
                    activitytxt = 'Transfered 1000 from Shares account to James (Account Number: 1234) today'
                    TransferHistory.objects.create( userAccName=senderobj.userID.firstName, userAccNo=senderobj.userAccNo,
                                                    accType=senderobj.acc_options, groupAccNo=senderobj.groupAccNo,
                                                    userAccBal=senderobj.userAccBal, amount=0, shares=amount,
                                                    activity=activitytxt, userAccBankBranch='Nyeri',
                                                    activityType='transfer', status='Successful' )

                    TransferHistory.objects.create( userAccName=recptobj.userID.firstName, userAccNo=recptobj.userAccNo,
                                                    accType=recptobj.acc_options, groupAccNo=recptobj.groupAccNo,
                                                    userAccBal=recptobj.userAccBal, amount=0, shares=amount,
                                                    activity=activitytxt, userAccBankBranch='Nyeri',
                                                    activityType='transfer', status='Successful' )

                    #######################################################################

                    context = {
                        'amount': amount,
                        'recepient': recptobj.userID,
                        'sender': senderobj.userID,
                        'senderbal': senderbal,
                        'senderobj': senderobj,
                        'transfer': 'Capital Equity (Shares)',
                    }
                    # return HttpResponseRedirect( reverse( 'transfer:confirm', ), context)
                    return render( request, 'transfer/confirm/index.html', context )
            else:
                ##################################################
                senderobj = get_object_or_404( User, pk__iexact=1 )
                ##################################################
                form = SharesForm()
                context = {
                    'form': form,
                    'senderobj': senderobj,
                    'error':'Wrong PIN'
                }
                # return HttpResponseRedirect( reverse('transfer:sharesHandler', ), context)
                return render( request, 'transfer/shares.html', context )

        # if a GET (or any other method) we'll create a blank form
    else:
        ###################################Replace with session
        senderobj = get_object_or_404( User, pk__iexact=1 )
        ######################################
        form = SharesForm()
        context = {
            'form': form,
            'senderobj':senderobj
        }
        #return HttpResponseRedirect( reverse('transfer:sharesHandler', ), context)
        return render( request, 'transfer/shares.html', context )

