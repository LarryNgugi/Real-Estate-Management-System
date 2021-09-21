from django.db import models

# Create your models here.

class Feedback (models.Model):
    message = models.TextField()
    first_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    phone_number = models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Feedback'