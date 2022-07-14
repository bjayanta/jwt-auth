from django.urls import path
from .views import SignupView, RetrieveUserView, VerifyOTP

urlpatterns = [
    path('', SignupView.as_view()),
    path('verify_otp/', VerifyOTP.as_view()),
    path('me/', RetrieveUserView.as_view()),
]
