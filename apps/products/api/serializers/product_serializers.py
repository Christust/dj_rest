from rest_framework import serializers
from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer

class ProductSerializer(serializers.ModelSerializer):

    # measure_unit = MeasureUnitSerializer()
    # category_product = CategoryProductSerializer()

    class Meta:
        model = Product
        exclude = ["state","created_date", "modified_date", "deleted_date"]

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "description": instance.description,
            "image": instance.image if instance.image != "" else None,
            "measure_unit": MeasureUnitSerializer(instance.measure_unit).data["description"],
            "category_product": CategoryProductSerializer(instance.category_product).data["description"],
        }