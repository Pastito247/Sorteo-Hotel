from django.urls import path
from .views import RegisterUser, VerifyEmail, LoginUser, SetPassword, ChooseWinner
from . import views

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('verify-email/<uidb64>/<token>/', VerifyEmail.as_view(), name='verify_email'),
    path('login/', LoginUser.as_view(), name='login'),
    path('set-password/', SetPassword.as_view(), name='set_password'),
    path('choose-winner/', ChooseWinner.as_view(), name='choose_winner'),
    path('send-email/', views.send_email_view, name='send_email'),
]
