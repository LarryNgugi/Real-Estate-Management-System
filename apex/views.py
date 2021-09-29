from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Feedback

# Create your views here.
def home(request):

    context ={
        
        'Phone':'0714389500',
        'Email' : 'larry.josephgithaka@gmail.com',
        'address':["513-10200","Nairobi,Kenya"],

    }

    return render(request, "home.html", context)

def contact(request):

    context ={}

    return render(request, "contact.html", context)

def profile(request):

    context ={
        
    }

    return render(request, "apex/admin/profile.html", context)


def saveFeedback(request):

    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    email = request.POST.get("email")
    phone_number = request.POST.get("number")
    message = request.POST.get("message")

    Feedback.objects.create(first_name=first_name,last_name=last_name, email=email,phone_number=phone_number, message=message)

    context = {}

    return HttpResponseRedirect('/contact')


def showFeedback(request):

    context = {}
    context['feedback_list'] = Feedback.objects.all()

    return render(request, 'apex/admin/feedback.html', context)
    
def deleteFeedback (request,id):

    our_feedback = Feedback.objects.get(pk = id)
    our_feedback.delete()

    return HttpResponseRedirect('/staff/feedback')