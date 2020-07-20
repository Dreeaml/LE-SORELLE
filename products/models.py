from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models

class Size(models.Model):
    size = models.CharField(max_length=20)

    class Meta:
        ordering = ['size']

    def __str__(self):
        return self.size
        
class Color(models.Model):
    color = models.CharField(max_length=20)

    class Meta:
        ordering = ['color']

    def __str__(self):
        return self.color

class Category(models.Model):
    category = models.CharField(max_length=40)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.category

class Product(models.Model):
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=40)
    description = tinymce_models.HTMLField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.ManyToManyField('Size')
    color = models.ManyToManyField('Color')
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Stock(models.Model):
    amount = models.PositiveIntegerField()
    product = models.ForeignKey('Product',null=True, on_delete=models.SET_NULL)
    size = models.ForeignKey('Size', null=True, on_delete=models.SET_NULL)
    color = models.ForeignKey('Color', null=True, on_delete=models.SET_NULL)

    unique_together = ('product', 'size', 'color')

class Image(models.Model):
    product = models.ForeignKey('Product', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=40, null=True)
    image = models.ImageField(upload_to="images")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
