from .models import Profile
import africastalking

username = 'sandbox'
api_key = 'c2cc8290d7985d228c31c7384f6f763ce6f0cff58abe7ad1f79e27ba04551aba'

africastalking.initialize(username, api_key)

sms = africastalking.SMS


def send_reminders():
    profiles = Profile.objects.all()
    for profile in profiles:
        invoice_message = f'Dear, {profile.name}, Your rent payment of shs {profile.amount} is due on demand. ' \
                          f'Please plan to pay before 5th using Buy Goods Till Number 717571. For queries call 0714389500 or email apexhomeskenya@gmail.com'
        response = sms.send(invoice_message, [str(profile.phone_number)])
        print(response)
