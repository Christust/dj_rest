from rest_framework import generics
from apps.products.models import MeasureUnit, Indicator, CategoryProduct
from apps.products.api.serializers.general_serializers import IndicatorSerializer, CategoryProductSerializer, MeasureUnitSerializer

class MeasureUnitListAPIView(generics.ListAPIView):
    queryset = MeasureUnit.objects.filter(state=True)
    serializer_class = MeasureUnitSerializer

class IndicatorListAPIView(generics.ListAPIView):
    queryset = Indicator.objects.filter(state=True)
    serializer_class = IndicatorSerializer

class CategoryProductListAPIView(generics.ListAPIView):
    queryset = CategoryProduct.objects.filter(state=True)
    serializer_class = CategoryProductSerializer
