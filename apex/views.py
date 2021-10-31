from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import ProfileForm, ProfilesForm
from .models import Feedback, Profile


# Create your views here.
from mpesa_api.models import MpesaPayment


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
            NextOfKinName = form.cleaned_data['NextOfKinName']
            NextOfKinId_number = form.cleaned_data['NextOfKinId_number']
            NextOfKinPhone_number = form.cleaned_data['NextOfKinPhone_number']
            NextOfKinEmail = form.cleaned_data['NextOfKinEmail']
            relationship = form.cleaned_data['relationship']

            Profile.objects.create(name=name, email=email, phone_number=phone_number, house_number=house_number
                                   , id_number=id_number, account_number=account_number, amount=amount,
                                   kin_name=NextOfKinName
                                   , kin_id_number=NextOfKinId_number, kin_phone_number=NextOfKinPhone_number,
                                   kin_email=NextOfKinEmail, relationship=relationship)

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


def updateProfile(request, id):
    our_profile = Profile.objects.get(pk=id)
    form = ProfilesForm(request.POST or None, instance=our_profile)

    if form.is_valid():
        form.save()

        return redirect('/staff/profile')

    return render(request, 'apex/admin/update.html', {'form': form, 'profile': our_profile})


def payment(request):
    context = {}
    context['payments_list'] = MpesaPayment.objects.all()

    return render(request, 'apex/admin/payment.html', context)
