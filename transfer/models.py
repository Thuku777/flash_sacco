from django.db import models
from django.utils import timezone
from user.models import User
from savings.models import Savings


class TransferHistory(models.Model):
    date = models.DateField(auto_now=True)
    userAccName = models.CharField( max_length=20, null=True )
    userAccNo = models.IntegerField(null=True)
    accType=models.CharField(max_length=30,null=True)
    groupAccNo=models.IntegerField(null=True)
    userAccBal = models.IntegerField(null=True)
    amount=models.IntegerField(null=True)
    shares=models.IntegerField(null=True)
    activity=models.CharField(max_length=200)
    userAccBankBranch = models.CharField( max_length=20,null=True )
    activityType = models.CharField( max_length=30 ,null=True)
    status=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.userAccName




