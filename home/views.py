from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product


class HomeView(ListView):
    """
    Displays the Home page.
    """
    model = Product
    template_name = 'home/index.html'
    context_object_name = 'products'
