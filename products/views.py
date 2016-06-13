from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from products.models import *

def index(request):
    itens = Item.objects.all
    return render(request, 'products/detail.html', {'itens': itens})

def increase_quantity(request):
    form = request.POST
    if form:
        id_item = form.get("id_item")
        qtd = int(form.get("quantity"))
        item = Item.objects.get(id=id_item)
        item.available_quantity = item.increase_quantity(qtd)
        item.save()
    return redirect(reverse("products:index"))

def decrease_quantity(request):
    form = request.POST
    if form:
        id_item = form.get("id_item")
        qtd = int(form.get("quantity"))
        item = Item.objects.get(id=id_item)
        item.available_quantity = item.decrease_quantity(qtd)
        item.save()
    return redirect(reverse("products:index"))
