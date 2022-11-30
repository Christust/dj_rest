from django.urls import path
from apps.products.api.views import general_views
from apps.products.api.views import product_views

urlpatterns = [

    # Urls administrativas
    path("measure_unit/", general_views.MeasureUnitListAPIView.as_view(), name="measure_unit"),
    path("indicator/", general_views.IndicatorListAPIView.as_view(), name="indicator"),
    path("category_product/", general_views.CategoryProductListAPIView.as_view(), name="category_product"),

    # CRUD Productos
    path("product/", product_views.ProductListCreateAPIView.as_view(), name="product_list_create"),
    path("product/<int:pk>", product_views.ProductRetrieveUpdateDestroyAPIView.as_view(), name="product_retrieve_update_destroy"),

]
