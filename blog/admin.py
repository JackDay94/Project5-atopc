from django.contrib import admin
from .models import BlogPost, BlogComment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BlogPost)
class BlogPostAdmin(SummernoteModelAdmin):
    """Admin for BlogPost"""
    list_display = (
        'title',
        'author',
        'slug',
        'status',
        'date_added',
    )

    prepopulated_fields = {
        'slug': ('title',)
        }

    list_filter = (
        'status',
    )

    search_fields = (
        'title',
    )

    summernote_fields = (
        'post_content',
    )


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    """Admin for BlogComment"""
    list_display = (
        'author',
        'post',
        'created_on',
    )

    list_filter = (
        'post',
    )

    search_fields = (
        'author',
        'post',
    )
