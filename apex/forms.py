from django import forms


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=50)
    phone_number = forms.IntegerField(widget=forms.NumberInput)
    house_number = forms.CharField(max_length=50)
    account_number = forms.CharField(max_length=50)
    amount = forms.IntegerField( widget=forms.NumberInput)
