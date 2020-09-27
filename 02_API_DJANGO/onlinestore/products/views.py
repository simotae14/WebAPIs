from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic import ListView

from products.models import Product, Manufacturer

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"

class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
