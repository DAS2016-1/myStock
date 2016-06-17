from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from products.models import *
from sales.models import *
from products.models import *
import datetime

def index(request):
    if request.method=="GET":
        products = Product.objects.all
        return render(request, 'sales/sales.html', {'products': products})
    else:
        form = request.POST
        form = form.dict()
        print(form)
        n_sale = Sale.objects.create(sale_date = datetime.datetime.now())
        for key, value in form.items():
            try:
                key = int(key)
                i = Product.objects.get(pk=key)
                item = Item.objects.create(item_product = i, sale = n_sale)
            except:
                pass

        products = Product.objects.all
        return render(request, 'sales/sales.html', {'products': products})

def list(request):
    list = Sale.objects.all
    return render(request, 'sales/list.html', {'list': list})
