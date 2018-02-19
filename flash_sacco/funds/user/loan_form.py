from django import forms

#

#copy of Applicant’s ID
#copy of the referee’s ID
#copy of Applicant’s PIN certificate
#all guarantors’ ID copies
#3 months’ certified pay slips
#3 months’ bank statements
#utility bill (not more than 3 months old)
#


class LoanForm (forms.Form ):
    applicantId = forms.IntegerField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off',
               'placeholder': 'Account Holders ID number'} ), label=' National ID' )

    refereeID = forms.IntegerField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off',
               'placeholder': 'Referees ID number'} ), label=' National ID' )

    guarantor=forms.CharField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder': 'Guarantors Name'} ),
                                    label='Guarantors Name' )

    amount = forms.IntegerField( widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': True, 'autocomplete': 'off', 'placeholder': 'Loan Amount'} ),
                                    label='Amount' )

    file_field = forms.FileField( widget=forms.ClearableFileInput( attrs=
                                                                   {'multiple': True, 'webkitdirectory': True,
                                                                    'directory': True} ) )

