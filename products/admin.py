from django.contrib import admin
from .models import Category, Product, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin for Category"""
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """Admin for Product"""
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
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

    summernote_fields = (
        'description',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin for Review"""
    list_display = (
        'author',
        'product',
        'rating',
        'created_on',
        'edited_on',
    )

    list_filter = (
        'author',
        'product',
        'created_on',
    )

    search_fields = (
        'product',
        'author',
    )
