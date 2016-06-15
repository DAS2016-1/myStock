from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from products.models import *
from sales.models import *

def index(request):
    products = Product.objects.all
    return render(request, 'sales/sales.html', {'products': products})
