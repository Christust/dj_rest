from datetime import timedelta
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

class ExpiringTokenAuthentication(TokenAuthentication):
    expired = False
    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds = 0)

    def token_expire_handler(self, token):
        is_expired = self.is_token_expired(token)
        if is_expired:
            self.expired = True
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user = user)
        return is_expired, token

    def authenticate_credentials(self, key):
        user, token, message = None, None, None
        try:
            token = self.get_model().objects.select_related("user").get(key = key)
            user = token.user
            if not user.is_active:
                message = "Usuario no existe"
            is_expired, token = self.token_expire_handler(token)
            if is_expired:
                message = "Token expirado"
        except self.get_model().DoesNotExist:
            message = "Token no existe"
            self.expired = True
        return (user, token, message, self.expired)