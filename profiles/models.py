from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.


class CustomUser(AbstractUser):
    """ Custom User Profile Class """

    username = None
    phone_number = models.CharField(max_length=100, unique=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.phone_number
