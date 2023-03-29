from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import BlogPost, BlogComment


class BlogPostForm(forms.ModelForm):
    """Form for blog posts"""
    class Meta:
        model = BlogPost
        fields = (
            'title',
            'subtitle',
            'post_content',
            'image_url',
            'blog_image',
            'status',
        )
        widgets = {
            'post_content': SummernoteWidget(),
        }


class BlogCommentForm(forms.ModelForm):
    """Form for blog comments"""
    class Meta:
        model = BlogComment
        fields = (
            'content',
        )
