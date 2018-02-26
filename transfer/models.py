

import datetime
from datetime import date

from django.db import models
from django.utils import timezone
from user.models import User
from savings.models import Savings

# Create your models here.


class Transfer(models.Model):
    pub_date = models.DateTimeField()
    amount = models.IntegerField()
    userAccNo = models.IntegerField()
    userAccType = models.CharField(max_length=10)
    userAccName = models.CharField(max_length=50)
    userAccBankBranch = models.CharField(max_length=20)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    savingsID = models.ForeignKey( Savings, on_delete=models.CASCADE)

    def __str__(self):
        return self.userAccName


class TransferHistory(models.Model):
    date = models.DateTimeField(null=True )
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

