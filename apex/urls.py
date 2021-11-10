"""apex_program URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.urls import path
from django.urls.conf import include
from apex import views
from mpesa_api import urls as mpesa_api_urls

staff_patterns = [
    path('feedback', views.showFeedback, name='feedback'),
    path('delete/feedback <id>', views.deleteFeedback, name='delete_feedback'),
    path('profile', views.profile, name='profile'),
    path('create/profile', views.saveProfile, name='save_form'),
    # path('delete/profile <id>', views.deleteProfile, name='delete_profile'),
    path('update/profile/<id>', views.updateProfile, name='update_profile'),
    path('nextofkin/profile', views.nextOfKin, name='nextOfKin'),
    path('payments', views.payment, name='payment'),
    path('inbox', views.inbox, name='inbox'),
    path('outbox', views.outbox, name='outbox'),
    path('create_sms/', views.create_sms, name="create_sms"),
    path('incoming_message/', views.incoming_message, name='incoming_message'),
    path('incoming_delivery_reports/', views.incoming_delivery_reports, name='incoming_delivery_reports'),
    path('delivery_reports', views.delivery_reports, name='delivery_reports'),

]

urlpatterns = [
    path('mpesa_api/', include(mpesa_api_urls)),
    path('staff/', include(staff_patterns)),
    path('', views.home, name='home'),
    path('contact/', views.contact, name="contact"),
    path('save_feedback', views.saveFeedback, name="save_feedback"),
    path('', views.logout, name="logouts"),

]
