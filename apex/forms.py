from django import forms

from .models import Profile

RELATIONSHIP_CHOICES = [
    ('Spouse', 'Spouse'),
    ('Father', 'Father'),
    ('Mother', 'Mother'),
    ('Guardian', 'Guardian'),
    ('Sibling', 'Sibling'),
    ('Other', 'Other'),
]


class ProfileForm(forms.Form):
    name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'placeholder': 'Tenant Full Name'}),
                           max_length=100)
    id_number = forms.IntegerField(label='ID Number',
                                   widget=forms.TextInput(attrs={'placeholder': 'Tenant National ID Number'}))
    phone_number = forms.IntegerField(label='Phone Number',
                                      widget=forms.TextInput(attrs={'placeholder': 'Tenant Official Phone Number'}))
    email = forms.EmailField(max_length=50, required=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Tenant Email (Optional) '}))
    house_number = forms.CharField(label='House Number', max_length=50,
                                   widget=forms.TextInput(attrs={'placeholder': 'Tenant House Number'}))
    account_number = forms.CharField(label='Account Number', max_length=50,
                                     widget=forms.TextInput(attrs={'placeholder': 'Tenant Account Number'}))
    amount = forms.IntegerField(label='House Amount',
                                widget=forms.TextInput(attrs={'placeholder': 'Tenant House Amount'}))
    NextOfKinName = forms.CharField(label='Next Of Kin Full Name',
                                    widget=forms.TextInput(attrs={'placeholder': 'Enter Next Of Kin Full Name'}),
                                    max_length=100)
    NextOfKinId_number = forms.IntegerField(label='Next Of Kin ID Number', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Next Of Kin National ID Number'}))
    NextOfKinPhone_number = forms.IntegerField(label='Next Of Kin Phone Number', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Next Of Kin Official Phone Number'}))
    NextOfKinEmail = forms.EmailField(label='Next Of Kin Email', required=False, max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Next Of Kin Email (Optional) '}))
    relationship = forms.CharField(label='Whats Your Relationship?', widget=forms.Select(choices=RELATIONSHIP_CHOICES))


class ProfilesForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'id_number', 'phone_number', 'email', 'house_number', 'account_number', 'amount',
                  'kin_name', 'kin_id_number', 'kin_phone_number', 'kin_email', 'relationship']
        labels = {
            'name': 'Name',
            'id_number': 'ID Number',
            'phone_number': 'Phone Number',
            'email': 'Email',
            'house_number': 'House Number',
            'account_number': 'Account Number',
            'amount': 'House Amount',
            'kin_name': 'Next Of Kin Full Name',
            'kin_id_number': 'Next Of Kin ID Number',
            'kin_phone_number': 'Next Of Kin Phone Number',
            'kin_email': 'Next Of Kin Email',
            'relationship': 'Relationship',
        }

        widgets = {

        }

