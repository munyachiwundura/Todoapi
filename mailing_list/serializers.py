from rest_framework import serializers
from mailing_list.models import MailItem


class MailItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailItem
        fields = "__all__"
