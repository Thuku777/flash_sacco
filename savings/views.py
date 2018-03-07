from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
#from transfer.models import TransferHistory
from django.urls import reverse
# Create your views here.


class SavingsRedirect(TemplateView):
    template_name = 'savings/index.html'

    def get_context_data(self, **kwargs):
        context=super(SavingsRedirect, self).get_context_data(**kwargs)
        context["title"]="This is a useless page"
        return context

 #sage=confirmTransfer(a, AccNo, AccBal, AccAmount, activity)
def confirmTransfer(self):
    #TransferHistory.objects.filter( userAccNo__exact=1234 ).update(userAccName='Women',userAccNo=1234, Acctype='personal', groupAccNo=1234,  userAccBal=123,amount=122, shares=0, activity='transfer',userAccBankBranch='nyc',activityType='transfer',status='works')
    return 'transfer complete'