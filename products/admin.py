from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'average_rating',
        'image',
    )

    list_filter = (
        'category',
    )

    search_fields = (
        'name',
        'sku',
        'category',
    )

    ordering = ('sku',)
