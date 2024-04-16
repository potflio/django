# your_app/views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def send_email_form(request):
    return render(request, 'send_email_form.html')

def send_email(request):
    if request.method == 'POST':
        recipient_email = request.POST.get('recipient_email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        sender_email = settings.EMAIL_HOST_USER  # Use your configured sender email

        try:
            send_mail(subject, message, sender_email, [recipient_email])
            messages.success(request, 'Email sent successfully!')
        except Exception as e:
            messages.error(request, f'Error sending email: {str(e)}')

        return redirect('send_email_form')

    return redirect('send_email_form')
