from rest_framework import serializers
from .models import CustomUser


# Serializer for User Model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name','phone_number','password']
