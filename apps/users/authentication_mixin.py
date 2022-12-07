from apps.users.authentication import ExpiringTokenAuthentication
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

class Authentication(object):

    user = None
    user_token_expired = False

    def get_user(self, request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
            except:
                return None
            token_expire = ExpiringTokenAuthentication()
            user, token, message, self.user_token_expired = token_expire.authenticate_credentials(token)
            if message == None:
                self.user = user
                return user
            else:
                return message
        return None

    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        if user is not None:
            if type(user) == str:
                response =  Response({"error":user, "expired":self.user_token_expired}, status=status.HTTP_401_UNAUTHORIZED)
                response.accepted_renderer = JSONRenderer()  # type: ignore
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                return response
            return super().dispatch(request, *args, **kwargs)  # type: ignore
        else:
            response = Response({"error":"No se encontraron las credenciales"})
            response.accepted_renderer = JSONRenderer()  # type: ignore
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            return response
    