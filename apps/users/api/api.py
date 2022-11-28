# Importamos Response para poder generar respuestas personalizadas
from rest_framework.response import Response
# Importamos status
from rest_framework import status
# APIView nos ayuda si queremos hacer clases en lugar de funciones para las vistas
from rest_framework.views import APIView
# El decorador @api_view nos ayuda si queremos usar funciones en lugar de clases
from rest_framework.decorators import api_view
# Importamos los serializers que hemos creados
from apps.users.api.serializers import UserSerializer, UserListSerializer
# Importamos nuestro modelo a usar para algunas ocasiones que se necesite
from apps.users.models import User
# Usamos la funcion get_object_or_404 cuando querramos usar un get sin try catch
from django.shortcuts import get_object_or_404

# class UserApiView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         user_serializer = UserSerializer(users, many=True)
#         return Response(user_serializer.data)

# Al decorador api_view le podemos proporcionar un array con los metodos http que permitira
@api_view(["GET", "POST"])
def user_api_view(request):
    
    # Se pregunta si el metodo es get o post, dependiendo del metodo aremos un retorno de los usuarios
    # o crearemos usuarios
    if request.method == "GET":
        
        # Buscamos los usaurios y los depositamos en una variable
        users = User.objects.all()
        
        # Instanciamos el serializer con el parametro many en True para indicar que seran
        # varios registros y guardamos en una variable
        user_serializer = UserListSerializer(users, many=True)

        # Retornamos un Response con la data del serializer y un status OK
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":

        # Instanciamos el serializer pero mediante el parametro data, esto indicara que se creara un registro
        # Si colocaramos instance y data al mismo tiempo indicariamos que se actualizara un registro
        # Si indicamos solo instance, entendera que ese registro ya existe y solo queremos pasarlo a json
        user_serializer = UserSerializer(data = request.data)

        # Utilizamos el metodo is_valid() para verificar si los datos recibidos son correctos
        if user_serializer.is_valid():

            # Usamos el metodo save() para guardar el registro del nuevo usuario
            user_serializer.save()

            # Retornamos la data del nuevo usuario y el estatus de creado
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:

            # Retornamos el estados de petición erronea
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Le proporcionamos get, put y delete para esta funcion ya que gestionara la edición
# el retorno de un usuario y la eliminación
# La funcion recibe ademas del request, la primary key (pk) para buscar al usuario
@api_view(["GET", "PUT", "DELETE"])
def user_detail_api_view(request, pk):

    # Buscamos al usuario mediante la pk
    user = get_object_or_404(User, id = pk)

    # Preguntamos que metodo se usa en el request, get para mostrar, put para editar y delete para borrar
    if request.method == "GET":

        # EL usuario encontrado se serializa
        user_serializer = UserSerializer(user)

        # Se retorna el usuario serializado con el estatus 200
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":

        # Se serializa el usuario y se pasa por segundo parametro la data
        # Esto hara que el serializador actualice el usuario en lugar de crear uno al usar el metodo
        # save()
        user_serializer = UserSerializer(user, request.data)

        # Preguntamos si es valido los datos recibidos
        if user_serializer.is_valid():

            # Guardamos los cambios en el usuario
            user_serializer.save()

            # Retornamos la data del usuario con el estatus 202
            return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)

        else:

            # Retornamos los errores y el estatus 400
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":

        # Solo borramos de forma directa al usuario por su pk que buscamos desde el inicio
        user.delete()

        # Retornamos un mensaje y el estatus 200
        return Response({"message":"Usuario eliminado"}, status=status.HTTP_200_OK)
