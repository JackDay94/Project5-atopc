from django.urls import path
from .views import HomeView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about_us/', views.about, name='about_us'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]
