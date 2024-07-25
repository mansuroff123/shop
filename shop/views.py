from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import Product

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'main/home.html'
    context_object_name = 'products'
    paginate_by = 1


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'

