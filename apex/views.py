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

def saveFeedback(request):

    name = request.POST.get("name")
    email = request.POST.get("email")
    phone_number = request.POST.get("number")
    message = request.POST.get("message")

    Feedback.objects.create(name=name, email=email,phone_number=phone_number, message=message)

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