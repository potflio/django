from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
from django.http import HttpResponse

@csrf_exempt
def sms_form(request):
    if request.method == "POST":
        to = request.POST.get('to')
        message_body = request.POST.get('message')

        # Twilio credentials
        account_sid = 'your_account_sid'
        auth_token = 'your_auth_token'
        from_number = '+1234567890'  # your Twilio number

        try:
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=message_body,
                from_=from_number,
                to=to
            )
            return HttpResponse("SMS sent successfully!")
        except Exception as e:
            return HttpResponse(f"Failed to send SMS: {e}")

    return render(request, 'sms_form.html')

def form(request):
    return render(request,"sms_form.html")
