from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import UpdateView

from .forms import ProfileForm, NextOfKinForm
from .models import Feedback, Profile, NextOfKin


# Create your views here.
def home(request):
    context = {

        'Phone': '0714389500',
        'Email': 'larry.josephgithaka@gmail.com',
        'address': ["513-10200", "Nairobi,Kenya"],

    }

    return render(request, "home.html", context)


def contact(request):
    context = {}

    return render(request, "contact.html", context)


def profile(request):
    context = {}
    context['profile_list'] = Profile.objects.all()

    return render(request, "apex/admin/profile.html", context)


def saveProfile(request):
    redirect_url = '/staff/profile'

    if request.method == 'POST':

        form = ProfileForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            id_number = form.cleaned_data['id_number']
            house_number = form.cleaned_data['house_number']
            account_number = form.cleaned_data['account_number']
            amount = form.cleaned_data['amount']

            Profile.objects.create(name=name, email=email, phone_number=phone_number, house_number=house_number
                                   , id_number=id_number, account_number=account_number, amount=amount)

            return HttpResponseRedirect(redirect_url)

    else:
        form = ProfileForm()

    return render(request, 'apex/admin/profile_form.html', {'form': form})


def deleteProfile(request, id):
    our_profile = Profile.objects.get(pk=id)
    our_profile.delete()

    return HttpResponseRedirect('/staff/profile')


def nextOfKin(request):
    context = {}

    context['nextofkin_list'] = Profile.objects.all()

    return render(request, 'apex/admin/NextOfKin.html', context)


def saveNextOfKin(request):
    redirect_url = '/staff/profile'

    if request.method == 'POST':

        form = NextOfKinForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            id_number = form.cleaned_data['id_number']

            NextOfKin.objects.create(name=name, email=email, phone_number=phone_number, id_number=id_number)

            return HttpResponseRedirect(redirect_url)

        else:
            form = NextOfKin()

        return render(request, 'apex/admin/profile_form.html', {'form': form})


def saveFeedback(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    email = request.POST.get("email")
    phone_number = request.POST.get("number")
    message = request.POST.get("message")

    Feedback.objects.create(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number,
                            message=message)

    context = {}

    return HttpResponseRedirect('/contact')


def showFeedback(request):
    context = {}

    context['feedback_list'] = Feedback.objects.all()

    return render(request, 'apex/admin/feedback.html', context)


def deleteFeedback(request, id):
    our_feedback = Feedback.objects.get(pk=id)
    our_feedback.delete()

    return HttpResponseRedirect('/staff/feedback')


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['name', 'id_number', 'phone_number', 'email', 'house_number', 'account_number', 'amount']
    success_url = '/staff/profile'
    template_name = 'apex/admin/update.html'
