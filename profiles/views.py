from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from rest_framework import viewsets, status
from rest_framework.response import Response

from rest_framework.views import APIView

from .models import CustomUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


## -------- Verification -------- ##
class VerifyCredentials(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        if not phone_number or not password:
            return Response({'error': 'Both phone number and password are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, phone_number=phone_number, password=password)

        if user:
            # If the user exists and the credentials are valid, return a token or any other response you want.
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # If the credentials are not valid, return an error response.
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
