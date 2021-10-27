from django import forms


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    ID_Number = forms.IntegerField(widget=forms.NumberInput)
    phone_number = forms.IntegerField(widget=forms.NumberInput)
    email = forms.EmailField(max_length=50)
    house_number = forms.CharField(max_length=50)
    account_number = forms.CharField(max_length=50)
    amount = forms.IntegerField( widget=forms.NumberInput)
