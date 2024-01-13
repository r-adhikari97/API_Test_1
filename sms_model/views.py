from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializer Models
from .serializers import SmsSerializers

# User Account
from .models import SMS

# Authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# API / Response Modules
from rest_framework import viewsets, status


## ------- Upload : Data Upload View ------- ##
class SMSViewset(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = SMS.objects.all()
    serializer_class = SmsSerializers


# APIView
class SMS_APIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Deserializing Data
        serializer = SmsSerializers(data=request.data)

        if serializer.is_valid():
            header = serializer.validated_data.get('header')
            body = serializer.validated_data.get('body')

            # Setting Custom Parameters
            serializer.validated_data['tsp'] = "A"
            serializer.validated_data['tsp'] = "B"
            serializer.validated_data['is_bank'] = True


            # Test
            print(f"{header} ---- {serializer.validated_data['tsp']} ----- {serializer.validated_data['tsp']} ----- {serializer.validated_data['is_bank']} -----{body}")

            # Saving Data
            serializer.save()

            # Output sent
            return Response({"output":serializer.validated_data['is_bank']}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



