# your_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('send-email/', views.send_email_form, name='send_email_form'),
    path('send-email/send/', views.send_email, name='send_email'),
]
