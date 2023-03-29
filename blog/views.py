from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView

from .models import BlogPost, BlogComment
from .forms import BlogPostForm, BlogCommentForm


class PostList(ListView):
    """Displays a list of blog posts"""
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-date_added')
    template_name = 'blog/blog.html'
    context_object_name = 'blog_posts'
    paginate_by = 8


class PostDetail(DetailView):
    """Displays the detail view of a blog post"""

    def get(self, request, slug, *args, **kwargs):
        queryset = BlogPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('-created_on')

        return render(
            request,
            "blog/blog_detail.html",
            {
                "blog_post": post,
                "comments": comments,
                "comment_form": BlogCommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = BlogPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('-created_on')
        
        comment_form = BlogCommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Comment added successfully!')
        else:
            comment_form = CommentForm()
            messages.error(request, 'Error! Comment was not added.')

        return render(
            request,
            "blog/blog_detail.html",
            {
                "blog_post": post,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )
