from django import forms


class TransferForm( forms.Form ):
    userAccName = forms.CharField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off',
               'placeholder': 'Account Name E.g Chama'} ), label='Account Name' )
    userAccNo = forms.IntegerField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder': 'Account Number'} ),
                                    label='Account Number' )
    recptAccNo = forms.IntegerField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off',
               'placeholder': 'Recepient Account Number'} ), label='Account Number' )
    userAccAmount = forms.IntegerField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder': 'Amount Ksh'} ),
                                        label='Amount' )
    userAccPasswd = forms.CharField( widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder': 'Account Password'} ),
                                     label='Password' )


class SharesForm( forms.Form ):
    senderAccNo = forms.IntegerField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder': 'Account Number'} ),
                                      label='My Account Number' )
    recpAccNo = forms.IntegerField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder': 'Account Number'} ),
                                    label='Recepient Account Number' )
    amount = forms.IntegerField( widget=forms.TextInput(
        attrs={'class': 'form-control unknown', 'required': True, 'autocomplete': 'off',
               'placeholder': 'Number of Shares'} ), label='Shares' )
    userAccPasswd = forms.CharField( widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder': 'Account Password'} ),
        label='Password' )
