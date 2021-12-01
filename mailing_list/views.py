from django.shortcuts import render
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from mailing_list.models import MailItem
from mailing_list.serializers import MailItemSerializer
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail as send_email
from django.template.loader import render_to_string
from django.conf import settings


# Create your views here.


@api_view(["POST"])
@csrf_exempt
def send_mail(request):
    serializer = MailItemSerializer(data=request.data)
    if serializer.is_valid():
        mail = serializer.save()
        msg_plain = f"Thank you {mail.name} for asking for my help with {mail.project_summary}, I look forword to working with {mail.company}. If Do not respond soon enough feel freee to dm me on  my socials"
        msg_html = render_to_string(
            "mailing_list/hire.html",
            {
                "name": mail.name,
                "project": mail.project_summary,
                "company": mail.company,
            },
        )
        send_email(
            mail.subject,
            msg_plain,
            settings.EMAIL_HOST_USER,
            [mail.email],
            fail_silently=False,
            html_message=msg_html,
        )
    return Response(serializer.data)


# @permission_classes([IsAuthenticated])
@api_view(["GET"])
def mail(request):
    mail_items = MailItem.objects.all()
    serializer = MailItemSerializer(mail_items, many=True)
    return Response(serializer.data)
