from apps.base.api import GeneralListApiView
from apps.products.api.serializers import general_serializers

class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = general_serializers.MeasureUnitSerializer

class IndicatorListAPIView(GeneralListApiView):
    serializer_class = general_serializers.IndicatorSerializer

class CategoryProductListAPIView(GeneralListApiView):
    serializer_class = general_serializers.CategoryProductSerializer
