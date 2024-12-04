def generate_verification_link(user):
    from django.utils.http import urlsafe_base64_encode
    from django.contrib.auth.tokens import default_token_generator
    from django.utils.encoding import force_bytes

    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    return f"http://localhost:5173/verify-email/{uid}/{token}/"
