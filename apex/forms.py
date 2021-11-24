from django import forms

from .models import Profile, Houses
from django.forms.widgets import NumberInput

RELATIONSHIP_CHOICES = [
    ('Spouse', 'Spouse'),
    ('Father', 'Father'),
    ('Mother', 'Mother'),
    ('Guardian', 'Guardian'),
    ('Sibling', 'Sibling'),
    ('Other', 'Other'),
]

HOUSE_CHOICES = [
    ('Single Room', 'Single Room'),
    ('Bedsitter', 'Bedsitter'),
    ('One Bedroom', 'One Bedroom'),
    ('Two Bedroom', 'Two Bedroom'),
    ('Three Bedroom', 'Three Bedroom'),
    ('Four Bedroom', 'Four Bedroom'),
    ('Other', 'Other'),
]

LOCATION_CHOICES = [
    ('Apex Apartment', 'Apex Apartment'),
    ('Nguwa Apartment', 'Nguwa Apartment'),
    ('Bethany Apartment', 'Bethany Apartment'),
    ('Kiharu Apartment', 'Kiharu Apartment'),
    ('Vidhu Apartment', 'Vidhu Apartment'),
    ('Other', 'Other'),
]

STATUS_CHOICES = [
    ('Occupied', 'Occupied'),
    ('Vacant', 'Vacant'),
]


class ProfileForm(forms.Form):
    name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'placeholder': 'Tenant Full Name'}),
                           max_length=100)
    id_number = forms.IntegerField(label='ID Number',
                                   widget=forms.TextInput(attrs={'placeholder': 'Tenant National ID Number'}))
    phone_number = forms.CharField(label='Phone Number',
                                   widget=forms.TextInput(attrs={'placeholder': 'Tenant Official Phone Number'}))
    house_number = forms.CharField(label='House Number', max_length=50,
                                   widget=forms.TextInput(attrs={'placeholder': 'Tenant House Number'}))
    account_number = forms.CharField(label='Account Number', max_length=50,
                                     widget=forms.TextInput(attrs={'placeholder': 'Tenant Account Number'}))
    amount = forms.CharField(label='House Amount',
                             widget=forms.TextInput(attrs={'placeholder': 'Tenant House Amount'}))
    date = forms.DateTimeField(label="Date Entered", required=True, widget=NumberInput(attrs={'type': 'date'}))
    NextOfKinName = forms.CharField(label='Next Of Kin Full Name', max_length=100,
                                    widget=forms.TextInput(attrs={'placeholder': 'Enter Next Of Kin Full Name'}))
    NextOfKinId_number = forms.IntegerField(label='Next Of Kin ID Number', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Next Of Kin National ID Number'}))
    NextOfKinPhone_number = forms.CharField(label='Next Of Kin Phone Number', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Next Of Kin Official Phone Number'}))
    relationship = forms.CharField(label='Whats Your Relationship?', widget=forms.Select(choices=RELATIONSHIP_CHOICES))


class ProfilesForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'id_number', 'phone_number', 'house_number', 'account_number', 'date', 'amount',
                  'kin_name', 'kin_id_number', 'kin_phone_number', 'relationship']
        labels = {
            'name': 'Name',
            'id_number': 'ID Number',
            'phone_number': 'Phone Number',
            'house_number': 'House Number',
            'account_number': 'Account Number',
            'amount': 'House Amount',
            'kin_name': 'Next Of Kin Full Name',
            'kin_id_number': 'Next Of Kin ID Number',
            'kin_phone_number': 'Next Of Kin Phone Number',
            'relationship': 'Relationship',
            'date': 'Date Entered'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Tenant Full Name'}),
            'id_number': forms.TextInput(attrs={'placeholder': 'Tenant National ID Number'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Tenant Official Phone Number'}),
            'house_number': forms.TextInput(attrs={'placeholder': 'Tenant House Number'}),
            'account_number': forms.TextInput(attrs={'placeholder': 'Tenant Account Number'}),
            'amount': forms.TextInput(attrs={'placeholder': 'Tenant House Amount'}),
            'kin_name': forms.TextInput(attrs={'placeholder': 'Enter Next Of Kin Full Name'}),
            'kin_id_number': forms.TextInput(attrs={'placeholder': 'Enter Next Of Kin National ID Number'}),
            'kin_phone_number': forms.TextInput(attrs={'placeholder': 'Enter Next Of Kin Official Phone Number'}),
            'relationship': forms.Select(choices=RELATIONSHIP_CHOICES),
            'date': forms.NumberInput(attrs={'type': 'date'}),
        }


class CreateSms(forms.Form):
    phone_number = forms.CharField(
        label='Phone Number',
        max_length=100,
        min_length=3,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'start with country code e.g +254xxx '}))
    message = forms.CharField(
        label='Message',
        max_length=255,
        min_length=3,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5, "cols": 20}))


class LoginForm(forms.Form):
    username = forms.CharField(label=None, max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}), min_length=3)

    password = forms.CharField(label=None, max_length=255, min_length=3, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))


class HousesForm(forms.Form):
    house_number = forms.CharField(label='House Number', max_length=50,
                                   widget=forms.TextInput(attrs={'placeholder': 'Tenant House Number'}))
    size = forms.CharField(label='House Type', max_length=20, widget=forms.Select(choices=HOUSE_CHOICES))
    amount = forms.IntegerField(label='House Amount',
                                widget=forms.TextInput(attrs={'placeholder': 'House Amount'}))
    location = forms.CharField(label='Location', widget=forms.Select(choices=LOCATION_CHOICES))
    status = forms.CharField(label='Status', widget=forms.Select(choices=STATUS_CHOICES))


class HouseForm(forms.ModelForm):
    class Meta:
        model = Houses

        fields = ['house_number', 'size', 'amount', 'location', 'status'
                  ]

        labels = {

            'house_number': 'House Number',
            'size': 'House Type',
            'amount': 'House Amount',
            'location': 'Location',
            'status': 'Status',

        }

        widgets = {
            'house_number': forms.TextInput(attrs={'placeholder': 'Tenant House Number'}),
            'size': forms.Select(choices=HOUSE_CHOICES),
            'location': forms.Select(choices=LOCATION_CHOICES),
            'amount': forms.TextInput(attrs={'placeholder': 'Tenant House Amount'}),
            'status': forms.Select(choices=STATUS_CHOICES),
        }


class CreateInvoiceForm(forms.Form):
    title = forms.CharField(label='Title', required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Title'}))

    amount = forms.IntegerField(label='Amount', required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Enter Invoice Amount'}))
    due_date = forms.DateTimeField(label='Due Date', required=True, widget=NumberInput(attrs={'type': 'date'}))
