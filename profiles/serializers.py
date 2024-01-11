from rest_framework import serializers
from .models import CustomUser


# Serializer for User Model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name','phone_number','password']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
