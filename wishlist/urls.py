from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('<product_id>/', views.add_remove_wishlist,
         name='add_remove_wishlist'),
]
