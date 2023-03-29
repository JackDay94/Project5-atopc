from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


class BlogPost(models.Model):
    """Model for the blog posts"""
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               related_name='post_author')
    date_added = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    blog_image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    post_content = models.TextField(max_length=2000)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    """Model for blog comments"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE,
                             related_name='comments')
    content = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment by {self.author}"
