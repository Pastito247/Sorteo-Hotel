from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_task(subject, message, from_email, to_email):
    # Enviar correo
    send_mail(
        subject,
        message,
        from_email,
        [to_email],
        fail_silently=False,
    )
    print(f"Correo enviado a: {to_email}")

