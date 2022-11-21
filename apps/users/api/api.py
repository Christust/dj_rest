from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.api.serializers import UserSerializer
from apps.users.models import User

# class UserApiView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         user_serializer = UserSerializer(users, many=True)
#         return Response(user_serializer.data)

@api_view(["GET", "POST"])
def user_api_view(request):
    if request.method == "GET":
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data)
    elif request.method == "POST":
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        else:
            return Response(user_serializer.errors, status=500)

@api_view(["GET"])
def user_detail_api_view(request, pk):
    if request.method == "GET":
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)