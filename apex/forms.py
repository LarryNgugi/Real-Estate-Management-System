from django import forms

class profileForms(forms.Forms):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=50)
    phone_number = forms.IntegerField(widget=forms.NumberInput)
    house_number = forms.CharField(max_length=50)
    
