from Account.models import KYC,Account
from django import forms 
from django.forms import ImageField,DateInput,FileInput


#date input 
class DateInput(forms.DateInput):
    input_type = 'date'


#Kyc Form
class KYCForm(forms.ModelForm):
    indetity_image = forms.ImageField(widget=FileInput)  # Correct the field name here
    profile_image = forms.ImageField(widget=FileInput)
    signature = forms.ImageField(widget=FileInput)

    class Meta:
        model = KYC 
        fields = ['fullname', 'profile_image', 'marital_status', 'gender', 'identity_type', 'indetity_image', 'country', 'city', 'date_of_birth', 'signature', 'state', 'mobile', 'fax']
        widgets = {
            'fullname': forms.TextInput(attrs={'placeholder': "Full Name"}),
            'country': forms.TextInput(attrs={'placeholder': "Country"}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'mobile': forms.TextInput(attrs={'placeholder': "Mobile"}),
            'fax': forms.TextInput(attrs={'placeholder': "Fax Number"}),
            'city': forms.TextInput(attrs={'placeholder': "City"}),
            'date_of_birth': DateInput
        }
