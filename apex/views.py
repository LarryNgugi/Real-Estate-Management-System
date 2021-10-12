from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Feedback, Profile
from django.views.generic.edit import CreateView
from apex.forms import ProfileForm

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

        'profileForm' : ProfileForm(),

        
    }

    return render(request, "apex/admin/profile.html", context)
    

def saveProfile(request):

    form = ProfileForm(request.POST)
    redirect_url ='/staff/profile'

    if form.is_valid():

        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phone_number']
        house_number = form.cleaned_data['house_number']
        amount = form.cleaned_data['amount']

        Profile.objects.create(name=name,email=email,phone_number=phone_number,amount=amount,house_number=house_number)

        return HttpResponseRedirect(redirect_url)

    else:

        form = ProfileForm()

        return HttpResponseRedirect(redirect_url, {'form': form})





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


