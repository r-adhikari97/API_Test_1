from rest_framework import serializers
from .models import SMS


# ------- SMS Serializer  -------- #
class SmsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SMS
        fields = "__all__"



