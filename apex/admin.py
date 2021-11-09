from .models import *
from .models import Outbox, Inbox, DeliveryReport
from django.contrib import admin

# Register your models here.

admin.site.register(Profile)
admin.site.register(Feedback)

admin.site.register(Outbox)
admin.site.register(Inbox)
admin.site.register(DeliveryReport)
