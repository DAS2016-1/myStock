from django.db import models
from products.models import *

class Sale(models.Model):
    sale_date = models.DateField()
    sale_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return "%s-%s" % (str(self.sale_date), str(self.id))
