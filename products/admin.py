from django.contrib import admin
from .models import *

admin.site.register(Provider)
admin.site.register(Brand)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Capacity)
admin.site.register(Measure)
admin.site.register(Volume)
admin.site.register(Package)
admin.site.register(Product)

# Register your models here.
