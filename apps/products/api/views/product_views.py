from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.products.api.serializers.product_serializers import ProductSerializer
from apps.users.authentication_mixin import Authentication

# ! Metodo sustituido por ListCreateAPIVIEW, en desuso
# Clase para Listar
# class ProductListAPIView(generics.ListAPIView):
#     serializer_class = ProductSerializer
#     queryset = serializer_class.Meta.model.objects.filter(state = True)
# 
# ! Metodo sustituido por ListCreateAPIVIEW, en desuso
# Clase para Crear
# class ProductCreateAPIView(generics.CreateAPIView):
#     serializer_class = ProductSerializer
# 
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer_class()
#         serializer = serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"mensaje":"Guardado con exito"}, status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
# 
# ! Metodo sustituido por RetrieveUpdateDestroyAPIView, en desuso
# Clase para Mostrar un registro
# class ProductRetrieveAPIView(generics.RetrieveAPIView):
#     serializer_class = ProductSerializer
#     queryset = serializer_class.Meta.model.objects.filter(state = True)
# 
# ! Metodo sustituido por RetrieveUpdateDestroyAPIView, en desuso
# Clase para Eliminar de forma logica un registro
# class ProductDestroyAPIView(generics.DestroyAPIView):
#     serializer_class = ProductSerializer
#     queryset = serializer_class.Meta.model.objects.filter(state = True)
# 
#     def delete(self, request, pk=None, *args, **kwargs):
#         product = self.get_queryset().filter(id = pk).first()
#         if product:
#             product.state = False
#             product.save()
#             return Response({"message":"Producto eliminado correctamente"}, status.HTTP_204_NO_CONTENT)
#         return Response({"message":"No se encontro el producto"}, status.HTTP_404_NOT_FOUND)
# 
# ! Metodo sustituido por RetrieveUpdateDestroyAPIView, en desuso
# Clase para Actualizar un registro
# class ProductUpdateAPIView(generics.UpdateAPIView):
#     serializer_class = ProductSerializer
#     queryset = serializer_class.Meta.model.objects.filter(state = True)
# 
# 
# ! Metodo sustituido por ProductViewSet, en desuso
# * ListCreateAPIView sustituye a ListAPIView y CreateAPIView 
# Clase para Listar y Crear
# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     serializer_class = ProductSerializer
#     queryset = serializer_class.Meta.model.objects.filter(state = True)
# ! Metodo sustituido por ProductViewSet, en desuso
# * RetrieveUpdateDestroyAPIView sustituye a RetrieveAPIView, UpdateAPIView y DestroyAPIView
# Clase para Mostrar, Actualizar y Eliminar de forma logica un registro
# class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductSerializer
#     queryset = serializer_class.Meta.model.objects.filter(state = True)

#     def delete(self, request, pk=None, *args, **kwargs):
#         product = self.get_queryset().filter(id = pk).first()
#         if product:
#             product.state = False
#             product.save()
#             return Response({"message":"Producto eliminado correctamente"}, status.HTTP_204_NO_CONTENT)
#         return Response({"message":"No se encontro el producto"}, status.HTTP_404_NOT_FOUND)


# La clase ModelViewSet generara un CRUD automaticamente solo colocando el serializador y el queryset, sobre escribimos los metodos que necesitemos tener con logica especifica.
# Heredamos de la clase Authentication para el metodo dispatch recibir el token.
class ProductViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = serializer_class.Meta.model.objects.filter(state = True)

    def destroy(self, request, pk=None, *args, **kwargs):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response({"message":"Producto eliminado correctamente"}, status.HTTP_204_NO_CONTENT)
        return Response({"message":"No se encontro el producto"}, status.HTTP_404_NOT_FOUND)