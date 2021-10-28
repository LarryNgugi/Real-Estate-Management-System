from django.db import models


# from mpesa_api.models import MpesaPayment


# Create your models here.

class NextOfKin(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    id_number = models.IntegerField(blank=False, null=True)
    house_number = models.CharField(max_length=10, blank=False, null=False)
    phone_number = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Next Of Kin'


class Profile(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    id_number = models.IntegerField(blank=False, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.IntegerField(blank=False, null=True)
    house_number = models.CharField(max_length=50, blank=False, null=True)
    account_number = models.CharField(max_length=50, blank=False, null=True)
    amount = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Profile'

    def __str__(self):
        return self.account_number


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
    phone_number = models.IntegerField(blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Feedback'
