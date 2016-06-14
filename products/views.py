from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from products.models import *
from decimal import Decimal

def index(request):
    itens = Item.objects.all
    return render(request, 'products/detail.html', {'itens': itens})

def increase_quantity(request):
    form = request.POST
    if form:
        id_item = form.get("id_item")
        qtd = int(form.get("quantity"))
        price = Decimal(form.get("price"))
        item = Item.objects.get(id=id_item)
        item.available_quantity = item.increase_quantity(qtd, price)
        item.save()
    return redirect(reverse("products:index"))

def decrease_quantity(request):
    form = request.POST
    if form:
        id_item = form.get("id_item")
        qtd = int(form.get("quantity"))
        price = Decimal(form.get("price"))
        item = Item.objects.get(id=id_item)
        item.available_quantity = item.decrease_quantity(qtd, price)
        item.save()
    return redirect(reverse("products:index"))
