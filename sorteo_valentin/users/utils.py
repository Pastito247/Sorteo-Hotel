from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

def generate_verification_link(user):
    from django.urls import reverse
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    link = reverse('verify_email', kwargs={'uidb64': uid, 'token': token})
    return f"http://127.0.0.1:8000{link}"
