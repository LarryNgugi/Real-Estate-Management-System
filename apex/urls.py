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
from django.urls import path
from django.urls.conf import include
from apex import views


staff_patterns = [
    path('feedback', views.showFeedback, name='feedback'),
    path('delete/feedback <id>',views.deleteFeedback,name='delete_feedback'),
    path('profile',views.profile,name='profile'),


]

urlpatterns = [
    path('staff/', include(staff_patterns)),
    path('', views.home, name='home'),
    path('contact/',views.contact, name="contact"),
    path ('save_feedback',views.saveFeedback, name = "save_feedback")

]
