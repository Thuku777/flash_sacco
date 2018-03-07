from django.db import models
from user.models import User

# Create your models here.


class Savings(models.Model):
    userID = models.ForeignKey( User, on_delete=models.CASCADE )
    userAccName = models.CharField( max_length=20 )
    userAccNo = models.IntegerField()
    userAccBal = models.IntegerField()
    groupAccNo = models.IntegerField()
    shares = 'shares'
    deposits = 'deposits'
    withdrawal_deposits = 'withdrawal deposits'
    savings_choices = (
    (shares, 'shares account'), (deposits, 'deposits account'), (withdrawal_deposits, 'withdrawal deposits account'))
    acc_options = models.CharField(
        max_length=50,
        choices=savings_choices,
    )

    def getshares(self):
        return self.shares_set.all()


    def __str__(self):
        return self.userAccName


class Shares(models.Model):
    savingsID = models.ForeignKey(Savings, on_delete=models.CASCADE )
    num_of_shares = models.IntegerField()


class Deposits( models.Model ):
    savingsID = models.ForeignKey( Savings, on_delete=models.CASCADE )
    num_of_shares = models.IntegerField()
    balance = models.IntegerField()


class WithdrawalDeposits( models.Model ):
    savingsID = models.ForeignKey( Savings, on_delete=models.CASCADE )
    balance = models.IntegerField()
    silver = 'silver'
    gold = 'gold'
    bronze = 'bronze'
    account_choices = ((gold, 'Gold Account'), (silver, 'Silver account'), (bronze, 'Bronze account'))
    acc_options = models.CharField(
        max_length=50,
        choices=account_choices,
    )


class Loans( models.Model ):
    savingsID = models.ForeignKey(Savings, on_delete=models.CASCADE)
    amount = models.IntegerField()
    deadline = models.DurationField()
    interest = models.FloatField()
    loanDate = models.DateField()
    normal = 'normal'
    emergency = 'emergency'
    fees = 'fees'
    loan_choices = ((normal, 'Normal Loan'), (emergency, 'Emergency Loan'), (fees, 'Fees Loan'))
    loan_options = models.CharField(
        max_length=50,
        choices=loan_choices
    )
