from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from random import choice
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import CustomUser
from .serializers import UserRegistrationSerializer
from .utils import generate_verification_link
from .serializers import UserLoginSerializer
from users.tasks import send_email_task



class RegisterUser(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            verification_link = generate_verification_link(user)
            # Usar Celery para enviar el correo con los datos correctos
            send_email_task.delay(
                'Verifica tu cuenta',
                f'Por favor, verifica tu correo haciendo clic en el siguiente enlace: {verification_link}',
                'HotelValentine@gmail.com',  # Remitente
                user.email  # Destinatario
            )
            return Response({"message": "User registered successfully. Check your email to verify your account."}, status=201)
        return Response(serializer.errors, status=400)

class VerifyEmail(APIView):
    def get(self, request, uidb64, token):
        print(f"UID: {uidb64}, Token: {token}")  # Para depuración
        try:
            from django.utils.http import urlsafe_base64_decode
            from django.utils.encoding import force_str
            from django.contrib.auth.tokens import default_token_generator
            from .models import CustomUser

            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            return Response({"error": "Invalid user ID."}, status=status.HTTP_400_BAD_REQUEST)

        if default_token_generator.check_token(user, token):
            user.is_email_verified = True
            user.save()
            return Response({"message": "Email verified successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):
    @csrf_exempt
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(request, username=email, password=password)

            if user is not None:
                if user.is_email_verified:
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'access_token': str(refresh.access_token),
                        'refresh_token': str(refresh),
                    })
                else:
                    return Response({"error": "Account is not verified yet."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class SetPassword(APIView):
    @csrf_exempt
    def post(self, request):
        serializer = SetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = CustomUser.objects.get(email=serializer.validated_data['email'])
                if user.is_email_verified:
                    user.set_password(serializer.validated_data['password'])
                    user.save()
                    return Response({"message": "Password set successfully."}, status=200)
                return Response({"error": "Email not verified."}, status=400)
            except CustomUser.DoesNotExist:
                return Response({"error": "User not found."}, status=404)
        return Response(serializer.errors, status=400)
    


class ChooseWinner(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        users = CustomUser.objects.filter(is_email_verified=True, is_active=True)
        
        if users.exists():
            winner = choice(users)  # Selección aleatoria
            # Llamamos a la tarea Celery para enviar el correo de felicitación
            send_email_task.delay(
                '¡Felicidades!',
                f'¡Felicidades {winner.username}! Has ganado el sorteo.',
                'HotelValentine@gmail.com', 
                winner.email  
            )
            return Response({"message": f"El ganador es: {winner.email}"})
        else:
            return Response({"error": "No eligible users found."}, status=400)

@csrf_exempt
def send_email_view(request):
    send_email_task.delay('test@example.com')
    return HttpResponse('El correo está siendo enviado')