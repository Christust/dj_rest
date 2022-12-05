# Importamos el modulo serializers de rest para crear nuestros serializadores
from rest_framework import serializers

# Importamos el modelo de nuestro usuario personalizado
from apps.users.models import User

# Creamos un serializador, una clase que hereda de ModelSerializer que nos ayudara a pasar a
# JSON todos los campos de nuestros modelos, asi podremos enviar y recibir objetos JSON
class UserSerializer(serializers.ModelSerializer):

    # Agregamos la clase Meta para nuestro metadatos
    class Meta:

        # Enlazamos el modelo User con este serializador
        model = User

        # Le indicamos que utilice todos los campos y los serialice
        # En caso de que querramos filtrar campos que devuelva nuestro serializer podemos
        # especificar cuales debe utilizar
        fields = "__all__"


    # La funcion create sera utilizada cada que llamemos a nuestro serializer y utilicemos
    # el metodo save del serializador e indiquemos solo el parametro data
    # Por ejemplo:
    #   user_serializer = UserSerializer(data = request.data)
    #   user_serializer.save()
    # Esto creara un nuevo registro de nuestro modelo
    def create(self, validated_data):

        # Instanciamos el modelo user con los datos validados, estos se validan con los
        # con los campos requeridos del modelo asi como con sus tipos
        user = User(**validated_data)

        # Encriptamos el password y lo depositamos en el parametro password
        user.set_password(validated_data["password"])

        # Guardamos el registro del nuevo usuario
        user.save()

        # Retornamos la instancia (esto es necesario para los serializers)
        return user

    # La funcion update sera utilizada cada que llamemos a nuestro serializer y utilicemos
    # el metodo save del serializador e indiquemos el parametro instance junto con el
    # parametro data
    # Por ejemplo:
    #   user = get_object_or_404(User, id = pk)
    #   user_serializer = UserSerializer(user, request.data)
    #   user_serializer.save()
    # Esto actualizara un registro de nuestro modelo
    def update(self, instance, validated_data):

        # Utilizamos el metodo update pero de la clase de la que heredamos, pasando la instancia y
        # los datos validados
        # Esto recorrera la instancia actualizando cada uno de los valores de los datos validados
        user = super().update(instance, validated_data)

        # Encriptamos la contraseña y la depositamos en el atributo password
        user.set_password(validated_data["password"])

        # Guardamos los cambios de nuestro usuario
        user.save()

        # Retornamos la instancia (esto es necesario para los serializers)
        return user
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "name", "last_name", "password"]

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "name", "last_name"]