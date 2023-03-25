from django.contrib import admin
from .models import Category, Product, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
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

    summernote_fields = (
        'description',
        'specification',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
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
