from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.base.api import GeneralListApiView
from apps.products.api.serializers.product_serializers import ProductSerializer

class ProductListAPIView(GeneralListApiView):
    serializer_class = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje":"Guardado con exito"}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = serializer_class.Meta.model.objects.filter(state = True)

class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = serializer_class.Meta.model.objects.filter(state = True)

    def delete(self, request, pk=None, *args, **kwargs):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response({"message":"Producto eliminado correctamente"}, status.HTTP_204_NO_CONTENT)
        return Response({"message":"No se encontro el producto"}, status.HTTP_404_NOT_FOUND)