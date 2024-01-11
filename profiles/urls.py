from django.urls import path,include
from .views import UserViewSet
from rest_framework import routers


# Using Router with VViewSet
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('',include(router.urls))
]