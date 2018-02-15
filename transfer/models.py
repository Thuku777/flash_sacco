import datetime
from datetime import date

from django.db import models
from django.utils import timezone


# Create your models here.


class Transfer(models.Model):
    pub_date = models.DateTimeField("Date this was published")
    amount = models.IntegerField()
    userAccNo = models.IntegerField()
    userAccType = models.CharField(max_length=10)
    userAccName = models.CharField(max_length=50)
    userAccBankBranch = models.CharField(max_length=20)

    def __str__(self):
        return self.userAccName


class Savings(models.Model):
    id = models.IntegerField(primary_key=True)
    #pub_date=models.DateTimeField(models.DateTimeField.auto_now)
    userAccName = models.CharField(max_length=20)
    userAccNo = models.IntegerField()
    userAccBal = models.IntegerField()

    def __str__(self):
        return self.userAccName
