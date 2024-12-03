from django.urls import path
from .views import RegisterUser, VerifyEmail, LoginUser

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('verify/<uidb64>/<token>/', VerifyEmail.as_view(), name='verify_email'),
    path('login/', LoginUser.as_view(), name='login'),
]
