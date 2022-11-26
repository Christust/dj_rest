from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel

# Create your models here.
class MeasureUnit(BaseModel):
    """Model definition for MeasureUnit."""

    # TODO: Define fields here
    description = models.CharField("Descripción", max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.change_by = value

    class Meta:
        """Meta definition for MeasureUnit."""

        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de medida'

    def __str__(self):
        """Unicode representation of MeasureUnit."""
        return self.description

class CategoryProduct(BaseModel):
    """Model definition for CategoryProduct."""

    # TODO: Define fields here
    description = models.CharField("Descripción", max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.change_by = value

    class Meta:
        """Meta definition for CategoryProduct."""

        verbose_name = 'Categoria de Producto'
        verbose_name_plural = 'Categorias de Producto'

    def __str__(self):
        """Unicode representation of CategoryProduct."""
        return self.description

class Indicator(BaseModel):
    """Model definition for Indicator."""

    # TODO: Define fields here
    descount_value = models.PositiveIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, verbose_name="Indicador de Ofertas", on_delete=models.CASCADE)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.change_by = value

    class Meta:
        """Meta definition for Indicator."""

        verbose_name = 'Indicador de oferta'
        verbose_name_plural = 'Indicadores de oferta'

    def __str__(self):
        """Unicode representation of Indicator."""
        return f"Oferta de la categoria {self.category_product} : {self.descount_value}%"

class Product(BaseModel):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField("Nombre del producto",max_length=50, unique=True, blank=False, null=False)
    description = models.CharField("Descripción", max_length=50, blank=False, null=False, unique=False)
    measure_unit = models.ForeignKey(MeasureUnit, verbose_name="Unidad de medida", on_delete=models.CASCADE, null=True)
    category_product = models.ForeignKey(CategoryProduct, verbose_name="Categoria de Producto", on_delete=models.CASCADE, null=True)
    # amount = models.IntegerField()
    image = models.ImageField("Imagen del producto", upload_to="products/", blank=True, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self,value):
        self.change_by = value

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name




