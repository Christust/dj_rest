from django.urls import path
from apps.products.api.views import general_views

urlpatterns = [

    # Urls administrativas
    path("measure_unit/", general_views.MeasureUnitListAPIView.as_view(), name="measure_unit"),
    path("indicator/", general_views.IndicatorListAPIView.as_view(), name="indicator"),
    path("category_product/", general_views.CategoryProductListAPIView.as_view(), name="category_product"),

]
