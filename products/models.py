from django.db import models
from sales.models import *
from django.utils import timezone

class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

class Provider(models.Model):
    provider_name = models.CharField(max_length=20)

    def __str__(self):
        return self.provider_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.brand_name)

class Capacity(models.Model):
    capacity = models.PositiveIntegerField(default=1) #Capacity of the pack. e.g.: 12, 24, 36

    def __str__(self):
        return str(self.capacity)

class Measure(models.Model):
    measure = models.CharField(max_length=10) #Unit of the package. e.g.: ml, l

    def __str__(self):
       return self.measure

class Volume(models.Model):
    volume = models.PositiveIntegerField() #Volume of the package. e.g.: 350

    def __str__(self):
       return str(self.volume)

class Package(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_type = models.CharField(max_length=30)

    def __str__(self):
        return self.package_type

class Product(models.Model):
    product_brand = models.ForeignKey(Brand)
    product_category = models.ForeignKey(Category)
    product_provider = models.ForeignKey(Provider)
    product_total_investment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    product_capacity = models.ForeignKey(Capacity)
    product_measure = models.ForeignKey(Measure)
    product_volume = models.ForeignKey(Volume)
    product_package = models.ForeignKey(Package)
    product_description = models.TextField()
    product_image_link = models.CharField(max_length=500)
    product_price = models.DecimalField(max_digits=5, decimal_places=2, default=000.00)
    available_quantity = models.PositiveIntegerField(default=0)
    minimum_quantity = models.PositiveIntegerField(default=5)

    def increase_quantity(self, qtd, price):
        self.available_quantity += qtd
        self.product_price = price
        self.product_total_investment += self.product_price * qtd
        return self.available_quantity

    def decrease_quantity(self, qtd, price):
        if (self.available_quantity - qtd) > 0:
            self.available_quantity -= qtd
            self.product_total_investment -= price * qtd
        else:
            self.available_quantity = 0
        return self.available_quantity

    def __str__(self):
        return "%s %s %s %s%s" % (self.product_category.category, self.product_brand,self.product_package, self.product_volume, self.product_measure)

class Item(models.Model):
    item_product = models.ForeignKey(Product)
    item_price = models.DecimalField(max_digits=5, decimal_places=2, default=000.00)
    sale = models.ForeignKey(Sale)

    def set_price(self):
        self.item_price = self.item_product.product_price

    def __str__(self):
        return str(self.item_product.product_brand)
