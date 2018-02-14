from django import forms

class TransferForm(forms.Form):
    userAccName=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'required':True, 'autocomplete':'off','placeholder':'Account Name E.g Chame'}),label='Account Name', max_length=50)
    userAccNo=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'required':True, 'autocomplete':'off','placeholder':'Account Number' }), label='Account Number')
    recptAccNo=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'required':True, 'autocomplete':'off','placeholder':'Recepient Account Number' }), label='Account Number')
    userAccAmount=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'required':True, 'autocomplete':'off','placeholder':'Amount Ksh'}), label='Amount')
    userAccPasswd=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'required':True, 'autocomplete':'off', 'placeholder':'Account Password'}), label='Password')