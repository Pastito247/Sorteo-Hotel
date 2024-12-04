from celery import shared_task
from django.core.mail import send_mail
from django.core.exceptions import ValidationError

@shared_task
def send_email_task(subject, message, from_email, to_email):
    try:
        # Intentar enviar el correo
        send_mail(
            subject,
            message,
            from_email,
            [to_email],  # Asegúrate de que sea una lista
            fail_silently=False,
        )
        print(f"Correo enviado a: {to_email}")
        return f"Correo enviado a: {to_email}"
    except Exception as e:
        # Capturar cualquier excepción durante el envío del correo
        print(f"Error al enviar correo a {to_email}: {e}")
        return f"Error al enviar correo a {to_email}: {e}"
