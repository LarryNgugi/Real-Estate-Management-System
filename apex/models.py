from django.db import models
from mpesa_api.models import MpesaPayment


# Create your models here.

class TenantDetails(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    house_number = models.CharField(max_length=10, blank=False, null=False)
    account_number = models.CharField(max_length=50, blank=False, null=True)
    Transaction = models.CharField(max_length=50, blank=True, null=False)
    phone_number = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.IntegerField(blank=False, null=True)
    house_number = models.CharField(max_length=50, blank=False, null=True)
    account_number = models.CharField(max_length=50, blank=False, null=True)
    amount = models.ForeignKey(MpesaPayment, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Profile'


class Account(models.Model):
    houseNumber = models.CharField(max_length=50, blank=False, null=True)
    accountNumber = models.CharField(max_length=50, blank=False, null=True)
    transaction = models.CharField(max_length=300, blank=True, null=False)
    name = models.CharField(max_length=100, blank=False, null=True)
    amount = models.IntegerField(default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Feedback(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Feedback'
