from django.contrib import messages
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import ProfileForm, ProfilesForm
from .models import Feedback, Profile, Houses
from mpesa_api.models import MpesaPayment
import datetime
from django.http import HttpResponse
from django.utils.timezone import make_aware
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from .forms import CreateSms
from .models import Outbox, Inbox, DeliveryReport
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def home(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('staff/profile')

    else:
        form = AuthenticationForm()

    return render(request, template_name="home.html", context={"form": form})


@login_required
def logout(request):
    auth_logout(request)
    messages.info(request, "Logged out successfully!")

    return HttpResponseRedirect("home.html")


def contact(request):
    context = {}

    return render(request, "contact.html", context)


@login_required
def profile(request):
    context = {}

    context['profile_list'] = Profile.objects.all()

    return render(request, "apex/admin/profile.html", context)


@login_required
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


@login_required
def deleteProfile(request, id):
    our_profile = Profile.objects.get(pk=id)
    our_profile.delete()

    return HttpResponseRedirect('/staff/profile')


@login_required
def nextOfKin(request):
    context = {}

    context['nextofkin_list'] = Profile.objects.all()

    return render(request, 'apex/admin/NextOfKin.html', context)


@login_required
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


@login_required
def showFeedback(request):
    context = {}

    context['feedback_list'] = Feedback.objects.all()

    return render(request, 'apex/admin/feedback.html', context)


@login_required
def deleteFeedback(request, id):
    our_feedback = Feedback.objects.get(pk=id)
    our_feedback.delete()

    return HttpResponseRedirect('/staff/feedback')


@login_required
def updateProfile(request, id):
    our_profile = Profile.objects.get(pk=id)
    form = ProfilesForm(request.POST or None, instance=our_profile)

    if form.is_valid():
        form.save()

        return redirect('/staff/profile')

    return render(request, 'apex/admin/update.html', {'form': form, 'profile': our_profile})


@login_required
def payment(request):
    context = {}
    context['payments_list'] = MpesaPayment.objects.all()

    return render(request, 'apex/admin/payment.html', context)


def houses(request):
    context = {}
    context['houses_list'] = Houses.objects.all()

    return render(request, 'apex/admin/house.html')


@login_required
def outbox(request):
    outbox = Outbox.objects.all()
    search_term = ''
    clicked = request.GET.get('clicked', 'outbox')
    if 'search' in request.GET:
        search_term = request.GET.get('search')
        outbox = outbox.filter(text__icontains=search_term)
    paginator = Paginator(outbox, 100)
    page = request.GET.get('page')
    outbox = paginator.get_page(page)
    context = {'outbox': outbox, 'active': clicked, 'search_term': search_term}
    return render(request, 'apex/admin/outbox.html', context)


@login_required
def create_sms(request):
    form = CreateSms()
    if request.method == "POST":
        form = CreateSms(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get("phone_number")
            message = form.cleaned_data.get("message")
            Outbox.send(phone_number, message)
            return redirect('outbox')
    return render(request, "apex/admin/createSms.html", {"form": form})


@csrf_exempt
@require_POST
def incoming_message(request):
    """
    sample incoming message from phone through AfricasTalking API
    {  'from': ['+254714389500'],
     'linkId': ['28a92cdf-2d63-4ee3-93df-4233d3de0356'],
       'text': ['heey this is a message from a phone'],
         'id': ['b68d0989-d856-494f-92ee-7c439e96e1d9'],
       'date': ['2021-01-14 08:10:15'],
         'to': ['2390'] }
    """
    date = request.POST.get('date')
    text = request.POST.get('text')
    phoneNo = request.POST.get('from')
    to = request.POST.get('to')
    linkId = request.POST.get('linkId')
    date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    aware_datetime = make_aware(date)
    Inbox_object = Inbox(
        date=aware_datetime,
        text=text,
        phone=phoneNo,
        to=to,
        linkId=linkId
    )
    Inbox_object.save()
    return HttpResponse(status=200)


@csrf_exempt
@require_POST
def incoming_delivery_reports(request):
    """
    sample delivery report from Africas Talking API
    {'phoneNumber': ['+254714389500'],
      'retryCount': ['0'],
          'status': ['Success'],
     'networkCode': ['63902'],
              'id': ['ATXid_29bc0ee2e3566472cd947d2f2918ab2f']}>
    """
    phoneNumber = request.POST.get('phoneNumber')
    retryCount = request.POST.get('retryCount')
    status = request.POST.get('status')
    networkCode = request.POST.get('networkCode')
    identifier = request.POST.get('id')
    DeliveryReport_object = DeliveryReport(identifier=identifier,
                                           phoneNumber=phoneNumber,
                                           retryCount=retryCount,
                                           status=status,
                                           networkCode=networkCode)
    DeliveryReport_object.save()
    return HttpResponse(status=200)


@login_required
def delivery_reports(request):
    clicked = request.GET.get('clicked')
    all_delivery_reports = DeliveryReport.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET.get('search')
        all_delivery_reports = all_delivery_reports.filter(identifier__icontains=search_term)
    paginator = Paginator(all_delivery_reports, 100)
    page = request.GET.get('page')
    all_delivery_reports = paginator.get_page(page)
    context = {'all_delivery_reports': all_delivery_reports, 'active': clicked, 'search_term': search_term}
    return render(request, "apex/admin/deliveryreports.html", context)


@login_required
def inbox(request):
    clicked = request.GET.get('clicked')
    all_inbox_items = Inbox.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET.get('search')
        all_inbox_items = all_inbox_items.filter(text__icontains=search_term)
    paginator = Paginator(all_inbox_items, 5)
    page = request.GET.get('page')
    all_inbox_items = paginator.get_page(page)
    context = {
        "all_inbox_items": all_inbox_items, 'active': clicked, 'search_term': search_term
    }
    return render(request, "apex/admin/inbox.html", context)

# Delivery report callback Url in AfricansTalking
# https://533d-105-163-2-125.ngrok.io/staff/incoming_delivery_reports/

# Inbox Url callback in AfricansTalking
# https://533d-105-163-2-125.ngrok.io/staff/incoming_message/
