from django import forms

RELATIONSHIP_CHOICES = [
    ('Spouse', 'Spouse'),
    ('Father', 'Father'),
    ('Mother', 'Mother'),
    ('Guardian', 'Guardian'),
    ('Sibling', 'Sibling'),
    ('Other', 'Other'),
]


class ProfileForm(forms.Form):
    name = forms.CharField(label='Full Name', max_length=100)
    id_number = forms.IntegerField(label='ID Number', widget=forms.NumberInput)
    phone_number = forms.IntegerField(label='Phone Number', widget=forms.NumberInput)
    email = forms.EmailField(max_length=50)
    house_number = forms.CharField(label='House Number', max_length=50)
    account_number = forms.CharField(label='Account Number', max_length=50)
    amount = forms.IntegerField(label='House Amount', widget=forms.NumberInput)


class NextOfKinForm(forms.Form):
    name = forms.CharField(label='Full Name', max_length=100)
    relationship = forms.CharField(label='Relationship', widget=forms.Select(choices=RELATIONSHIP_CHOICES))
    ID_Number = forms.IntegerField(label='ID Number', widget=forms.NumberInput)
    email = forms.EmailField(max_length=50)
    phone_number = forms.IntegerField(label='Phone Number', widget=forms.NumberInput)
