from django.urls import path
from mailing_list import views

urlpatterns = [
    path("send", views.send_mail, name="Send Me Mail"),
    path("inbox", views.mail, name="My Inbox"),
]
