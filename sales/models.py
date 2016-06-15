from django.db import models
from products.models import *

class Sale(models.Model):
    sale_date = models.DateField()
