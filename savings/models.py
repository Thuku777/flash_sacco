from django.db import models

# Create your models here.

class Savings(models.Model):
    id = models.IntegerField(primary_key=True)
    #pub_date=models.DateTimeField(models.DateTimeField.auto_now)
    userAccName = models.CharField(max_length=20)
    userAccNo = models.IntegerField()
    userAccBal = models.IntegerField()

    def __str__(self):
        return self.userAccName
