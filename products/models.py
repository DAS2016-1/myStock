from django.db import models
from django.utils import timezone

class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

class Provider(models.Model):
    provider_name = models.CharField(max_length=20)

    def __str__(self):
        return self.provider_name

class Product(models.Model):
    product = models.CharField(max_length=50)
    product_category = models.ForeignKey(Category)
    product_provider = models.ForeignKey(Provider)

    def __str__(self):
        return self.product

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

class Item(models.Model):
    item_name = models.ForeignKey(Product)
    item_price = models.DecimalField(max_digits=5, decimal_places=2, default=000.00)
    item_total_investment = models.DecimalField(max_digits=10, decimal_places=2)
    item_capacity = models.ForeignKey(Capacity)
    item_measure = models.ForeignKey(Measure)
    item_volume = models.ForeignKey(Volume)
    item_package = models.ForeignKey(Package)
    item_description = models.TextField()
    available_quantity = models.PositiveIntegerField(default=0)
    minimum_quantity = models.PositiveIntegerField(default=5)
    item_image_link = models.CharField(max_length=500)

    def increase_quantity(self, qtd, price):
        self.available_quantity += qtd
        self.item_price = price
        self.item_total_investment += self.item_price * qtd
        return self.available_quantity

    def decrease_quantity(self, qtd, price):
        if (self.available_quantity - qtd) > 0:
            self.available_quantity -= qtd
            self.item_total_investment -= price * qtd
        else:
            self.available_quantity = 0
        return self.available_quantity

    def __str__(self):
        return self.item_name.product
