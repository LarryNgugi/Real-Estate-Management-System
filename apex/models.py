import requests
from django.db import models
from django.conf import settings
import datetime


# Create your models here.
class Houses(models.Model):
    house_number = models.CharField(max_length=50, blank=False, null=True)
    size = models.CharField(max_length=50, blank=False, null=True)
    amount = models.IntegerField(default=0, blank=False, null=False)
    location = models.CharField(max_length=50, blank=False, null=True)
    status = models.CharField(max_length=50, blank=False, null=True)

    class Meta:
        verbose_name_plural = 'Houses'

    def __str__(self):
        return self.house_number


class Profile(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    kin_name = models.CharField(max_length=100, blank=False, null=True)
    id_number = models.IntegerField(blank=False, null=True)
    kin_id_number = models.IntegerField(blank=False, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    kin_phone_number = models.CharField(max_length=15, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=False, null=True)
    amount = models.IntegerField(blank=True, null=True)
    relationship = models.CharField(max_length=100, blank=False, null=True)
    house_number = models.CharField(max_length=50, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(null=True)

    class Meta:
        verbose_name_plural = 'Profile'

    def __str__(self):
        return self.name


class Account(models.Model):
    houseNumber = models.CharField(max_length=50, blank=False, null=True)
    accountNumber = models.CharField(max_length=50, blank=False, null=True)
    transaction = models.CharField(max_length=300, blank=True, null=False)
    name = models.CharField(max_length=100, blank=False, null=True)
    amount = models.IntegerField(default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Account'


class Feedback(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Feedback'


def increment_invoice_number():
    last_invoice = Invoice.objects.all().order_by('id').last()
    if not last_invoice:
        return 'PLB0001'
    invoice_no = last_invoice.invoice_no
    invoice_int = int(invoice_no.split('PLB')[-1])
    width = 4
    new_invoice_int = invoice_int + 1
    formatted = (width - len(str(new_invoice_int))) * "0" + str(new_invoice_int)
    new_invoice_no = 'PLB' + str(formatted)
    return new_invoice_no


class Invoice(models.Model):
    title = models.CharField(max_length=30, blank=False, null=True)
    status = models.CharField(max_length=30, blank=False, null=True)
    house_number = models.CharField(max_length=50, blank=False, null=True)
    name = models.ForeignKey(Profile, on_delete=models.CASCADE, max_length=100, blank=False, null=True, related_name="profile_name")
    due_date = models.DateField(blank=False, null=True)
    phone_number = models.ForeignKey(Profile, on_delete=models.CASCADE,max_length=15, blank=True, null=True)
    amount = models.IntegerField(default=0, blank=False, null=False)
    invoice_no = models.CharField(max_length=500, default=increment_invoice_number, null=True, blank=True)

    class Meta:
        ordering = ['invoice_no', ]


class Outbox(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    statusCode = models.IntegerField()
    phone = models.CharField(max_length=15)
    text = models.CharField(max_length=255)
    messageId = models.CharField(max_length=100)

    class Meta:
        ordering = ('-date',)
        verbose_name = ("Outbox")
        verbose_name_plural = ("Outbox")

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.messageId, self.status, self.text[:10])  # noqa: E501

    @staticmethod
    def send(phone_number, message):
        url = settings.AT_ENDPOINT_URL
        headers = {'ApiKey': settings.AT_API_KEY,
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Accept': 'application/json'}
        body = {'username': settings.AT_USER_NAME,
                'from': settings.AT_FROM_VALUE,
                'message': message,
                'to': phone_number}
        response = requests.post(url=url, headers=headers, data=body)
        data = response.json().get('SMSMessageData').get('Recipients')[0]
        Outbox_object = Outbox(status=data['status'],
                               statusCode=data['statusCode'],
                               phone=data['number'],
                               text=message,
                               messageId=data['messageId'])
        Outbox_object.save()


class Inbox(models.Model):
    date = models.DateTimeField(null=True, blank=True)
    text = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    to = models.IntegerField()
    linkId = models.CharField(max_length=100)

    class Meta:
        ordering = ('-date',)
        verbose_name = ("Inbox")
        verbose_name_plural = ("Inbox")

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.linkId, self.phone, self.text[:10])  # noqa: E501


class DeliveryReport(models.Model):
    identifier = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    phoneNumber = models.CharField(max_length=15)
    retryCount = models.IntegerField()
    status = models.CharField(max_length=10, blank=True, null=True)
    networkCode = models.IntegerField()

    class Meta:
        ordering = ('-date',)
        verbose_name = ("Delivery Report")
        verbose_name_plural = ("Delivery Reports")

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.identifier, self.phoneNumber, self.status)
