from django.db import models

# Create your models here.
class Category(models.Model):
    nombCategory = models.CharField(max_length=140)
    def __str__(self):
        return self.nombCategory
    class Meta:
        verbose_name_plural = 'Categoria'

class Producto(models.Model):
    nombProduc = models.CharField(max_length=130)
    descripcion = models.CharField(max_length=80)
    Categoria = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imgProduc = models.ImageField(upload_to='uploads/products/')


