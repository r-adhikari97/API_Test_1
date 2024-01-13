from django.urls import path,include
from .views import SMSViewset, SMS_APIView
from rest_framework import routers


# Using Router with VViewSet
router = routers.DefaultRouter()
router.register(r'upload', SMSViewset)

urlpatterns = [
    path('',include(router.urls)),
    path("Test_View/",SMS_APIView.as_view(),name="TEST_API_UPLOAD")
]