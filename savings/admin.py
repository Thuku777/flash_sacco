from django.contrib import admin
from .models import Savings, Shares, Deposits, WithdrawalDeposits, Loans

# Register your models here.
admin.site.register(Savings)
admin.site.register(Shares)
admin.site.register(Deposits)
admin.site.register(WithdrawalDeposits)
admin.site.register(Loans)