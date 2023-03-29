from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from blog.models import BlogPost


class HomeView(ListView):
    """
    Displays the Home page.
    """
    model = Product, BlogPost
    template_name = 'home/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = {
            'new_products': Product.objects.order_by(
                '-date_added')[0:4],
            'top_peripherals': (
                Product.objects.filter(category__name="keyboards") |
                Product.objects.filter(category__name="mice") |
                Product.objects.filter(category__name="headphones")
                ).order_by('-average_rating')[0:4],
            'top_monitors': (
                Product.objects.filter(category__name="1080p_monitors") |
                Product.objects.filter(category__name="1440p_monitors") |
                Product.objects.filter(category__name="4k_monitors")
                ).order_by('-average_rating')[0:4],
            'top_storage': (
                Product.objects.filter(category__name="hard_drives") |
                Product.objects.filter(category__name="solid_state_drives")
                ).order_by('-average_rating')[0:4],
            'latest_posts': (
                BlogPost.objects.filter(status=1).order_by('-date_added')[:4]
            )
        }
        return queryset


def about(request):
    """
    Displays the about us page.
    """

    return render(request, "home/about.html")
