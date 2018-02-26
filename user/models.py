import datetime
from datetime import date

from django.db import models
from django.utils import timezone


# Create your models here.

class Group( models.Model ):
    groupAccName = models.CharField( max_length=100 )
    groupAccNo = models.IntegerField()
    groupAccBal = models.IntegerField()

    def __str__(self):
        return self.groupAccName


class User( models.Model ):
    # group = models.ForeignKey( Group, on_delete=models.CASCADE )
    #group = models.ForeignKey( Group, on_delete=models.CASCADE , null=True)
    register_date = models.DateTimeField()
    firstName = models.CharField( max_length=20 )
    lastName = models.CharField( max_length=20 )
    IDnumber = models.IntegerField()
    #userAccNo = models.IntegerField()
    contact = models.IntegerField()
    email = models.EmailField( max_length=50 )
    DateOfBirth = models.DateField()
    address = models.CharField( max_length=50 )
    code = models.IntegerField()
    town = models.CharField( max_length=30 )
    accountPin = models.IntegerField()
    married_choices = (
        ('single', 'single'),
        ('married', 'married'),
    )
    marital = models.CharField( max_length=10, choices=married_choices )
    employed = models.BooleanField()
    image = models.ImageField()
    #male = 'Male'
    #female = 'Female'
    #gender_choices = ((male, 'Male'), (female, 'Female'))
    #gender = models.CharField(   max_length=20, choices=gender_choices,)
    #groupID=models.IntegerField(null=True)


    def __str__(self):
        return self.firstName
