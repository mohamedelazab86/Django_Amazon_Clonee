from django.shortcuts import render
from .models import Product,Brand,Review,ProductImage
from django.views.generic import ListView,DetailView

# Create your views here.

# ------------- create crud opertions by class based view ---------------------

class ProductList(ListView):
    model=Product

class ProctDetail(DetailView):
    model=Product
