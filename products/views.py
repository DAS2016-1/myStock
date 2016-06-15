from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from products.models import *
from decimal import Decimal

def index(request):
    products = Product.objects.all
    return render(request, 'products/detail.html', {'products': products})

def increase_quantity(request):
    form = request.POST
    if form:
        id_product = form.get("id_product")
        qtd = int(form.get("quantity"))
        price = Decimal(form.get("price"))
        product = Product.objects.get(id=id_product)
        product.available_quantity = product.increase_quantity(qtd, price)
        product.save()
    return redirect(reverse("products:index"))

def decrease_quantity(request):
    form = request.POST
    if form:
        id_product = form.get("product_item")
        qtd = int(form.get("quantity"))
        price = Decimal(form.get("price"))
        product = Product.objects.get(id=id_product)
        product.available_quantity = product.decrease_quantity(qtd, price)
        product.save()
    return redirect(reverse("products:index"))
