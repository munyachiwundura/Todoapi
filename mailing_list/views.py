from django.shortcuts import render
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from mailing_list.models import MailItem
from mailing_list.serializers import MailItemSerializer
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail as send_email


# Create your views here.


@api_view(["POST"])
@csrf_exempt
def send_mail(request):
    serializer = MailItemSerializer(data=request.data)
    if serializer.is_valid():
        mail = serializer.save()
        send_email(
            mail.subject,
            mail.project_summary,
            "from@example.com",
            [mail.email],
            fail_silently=False,
        )
    return Response(serializer.data)


# @permission_classes([IsAuthenticated])
@api_view(["GET"])
def mail(request):
    mail_items = MailItem.objects.all()
    serializer = MailItemSerializer(mail_items, many=True)
    return Response(serializer.data)
