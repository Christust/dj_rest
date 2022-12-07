from datetime import datetime
from django.contrib.sessions.models import Session
from rest_framework.authtoken. views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from apps.users.api.serializers import UserTokenSerializer


# Creamos una clase llamada Login heredando de ObtainAuthToken
class Login(ObtainAuthToken):

    # Definimos el metodo post para enviar el token cuando recibamos el post
    def post(self, request, *args, **kwargs):
        # Se utiliza el serializador de la clase, recibiendo la request.
        # Se envia el contexto como request
        login_serializer = self.serializer_class(data = request.data, context = {"request":request})

        # Preguntamos si es valido la data mandada
        if login_serializer.is_valid():

            # Depositamos el user obteniendolo de validated data 
            user = login_serializer.validated_data["user"]  # type: ignore

            # Verificamos user si es que esta activo
            if user.is_active:

                # Depositamos el token y el created de la clase Token, si no existe lo creamos
                token, created = Token.objects.get_or_create(user = user)

                # Serializamos el usuario con el Serializador creado
                user_serializer = UserTokenSerializer(user)

                # Preguntamos si fue creado
                if created:

                    # Retornamos la respuesta con la key del token, el usuario, y un mensaje
                    return Response({"token":token.key, "user": user_serializer.data, "message":"Inicio de sesion exitoso"}, status=status.HTTP_201_CREATED)
                else:

                    # Depositamos todas las sesiones obteniendolas del modelo y que su fecha de
                    # expiración sea mayor o igual que el momento de su consulta
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())

                    # Preguntamos si existen las sesiones
                    if all_sessions.exists():

                        # Recorremos las sesiones
                        for session in all_sessions:

                            # Obtenemos la data con get_decoded()
                            session_data = session.get_decoded()

                            # Preguntamos si el id del usuario es igual que el atributo
                            # _auth_user_id 
                            if user.id == int(session_data.get("_auth_user_id")):

                                # Borramos la session
                                session.delete()

                    # Borramos el token
                    token.delete()

                    # Generamos un token nuevo
                    token = Token.objects.create(user=user)

                    # Retornamos el key del token, el usuario y un mensaje
                    return Response({"token":token.key, "user": user_serializer.data, "message":"Inicio de sesion exitoso"}, status=status.HTTP_201_CREATED)

            else:

                # Retornamos un mensaje de error de que no esta activo
                return Response({"error":"Este usuario no puede iniciar sesion"}, status=status.HTTP_401_UNAUTHORIZED)
        else:

            # Retornamos un error de que las credenciales estan incorrectas
            return Response({"error":"Nombre de usuario o contraseña incorrectos"}, status=status.HTTP_400_BAD_REQUEST)


# Creamos una clase para el logout que hereda de APIView
class Logout(APIView):

    # Definimos el metodo post
    def post(self, request, *args, **kwargs):

        # Utilizamos un try para capturar los posibles errores
        try:

            # Obtenemos el token enviado de la data del request
            token = request.data["token"]

            # Obtenemos el token del modelo token
            token = Token.objects.filter(key = token).first()

            # Verificamos si existe
            if token:

                # Obtenemos el usuario a partir del token
                user = token.user

                # Depositamos todas las sesiones obteniendolas del modelo y que su fecha de
                # expiración sea mayor o igual que el momento de su consulta
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())

                # Preguntamos si existen las sesiones
                if all_sessions.exists():

                    # Recorremos las sesiones
                    for session in all_sessions:

                        # Obtenemos la data con get_decoded()
                        session_data = session.get_decoded()

                        # Preguntamos si el id del usuario es igual que el atributo
                        # _auth_user_id
                        if user.id == int(session_data.get("_auth_user_id")):

                            # Borramos la session
                            session.delete()

                # Borramos el token
                token.delete()

                # Guardamos mensaje
                session_message = "Sesiones de usuario eliminadas"

                # Guardamos mensaje de token
                token_message = "Token eliminado"

                # Devolvemos una respuesta con los mensajes
                return Response({"token_message":token_message, "session_message":session_message}, status=status.HTTP_200_OK)

            # Retornamos un mensaje de que el token no fue encontrado
            return Response({"error":"No se encontro usuario con este token"}, status=status.HTTP_404_NOT_FOUND)

        except:

            # Retornamos una respuesta de que no se encontro el token
            return Response({"error":"No se encontro token"}, status=status.HTTP_409_CONFLICT)

class UserToken(APIView):
    def get(self, request, *args, **kwargs):
        username = request.GET.get("username")
        try:
            user_token = Token.objects.get(
                user = UserTokenSerializer().Meta.model.objects.filter(username = username).first())
            return Response({"token":user_token.key})
        except:
            return Response({"error":"Credenciales enviadas incorrectas"}, status=status.HTTP_400_BAD_REQUEST)