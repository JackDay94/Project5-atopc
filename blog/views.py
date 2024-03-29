from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy

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
            comment_form = BlogCommentForm()
            messages.error(request, 'Error! Comment was not added.')

        return render(
            request,
            "blog/blog_detail.html",
            {
                "blog_post": post,
                "comments": comments,
                "comment_form": BlogCommentForm()
            },
        )


class AddPost(UserPassesTestMixin, CreateView):
    """Allows a superuser to add a blog post"""
    model = BlogPost
    form_class = BlogPostForm
    form = BlogPostForm()
    template_name = 'blog/add_post.html'

    def post(self, request):
        if request.method == "POST":
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.author = self.request.user
                new_post.slug = slugify(new_post.title)
                new_post.save()
                messages.success(request, 'Blog post was added successfully!')
                if new_post.status == 1:
                    return redirect(reverse_lazy(
                                    'post_detail', args=[new_post.slug]))
                else:
                    return redirect("blog")
            else:
                messages.error(request, 'Could not add the blog post!')

        return redirect("blog")

    def test_func(self):
        return self.request.user.is_superuser


class EditPost(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """Allows a superuser to edit a blog post"""
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/edit_post.html'
    success_message = 'You have updated the post successfully!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_title'] = self.object.title
        messages.info(self.request, f'You are editing {self.object.title}')

        return context

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        if self.object.status == 1:
            return reverse_lazy('post_detail', args=[self.object.slug])
        else:
            return reverse_lazy('blog')


class DeletePost(UserPassesTestMixin, DeleteView):
    """Allows a superuser to delete a blog post"""
    model = BlogPost
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog')
    success_message = 'You have deleted the Blog post successfully!'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_title'] = self.object.title
        messages.info(self.request, f'You are about to delete \
                     {self.object.title}')

        return context

    # Success message on delete taken from:
    # https://stackoverflow.com/questions/48777015/djangos-successmessagemixin-not-working-with-deleteview
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message, 'danger')

        return super(DeletePost, self).delete(request, *args, **kwargs)


class EditComment(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """Allows a user to edit their comment"""
    model = BlogComment

    fields = [
        'content',
    ]

    template_name = 'blog/edit_comment.html'
    success_message = 'Updated Comment successfully!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_title'] = self.object.post
        messages.info(self.request, f'You are editing your comment for \
                     {self.object.post}')

        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def test_func(self):
        author = self.get_object().author
        return self.request.user.is_superuser or self.request.user == author

    def get_success_url(self):
        return reverse_lazy('post_detail', args=[self.object.post.slug])


class DeleteComment(UserPassesTestMixin, DeleteView):
    """Allows a user to delete their comment"""
    model = BlogComment
    template_name = 'blog/delete_comment.html'
    success_message = 'Comment deleted succesfully!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_title'] = self.object.post
        messages.info(self.request, f'You are deleting your comment for \
                     {self.object.post}')

        return context

    # Success message on delete taken from:
    # https://stackoverflow.com/questions/48777015/djangos-successmessagemixin-not-working-with-deleteview
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message, 'danger')

        return super(DeleteComment, self).delete(request, *args, **kwargs)

    def test_func(self):
        author = self.get_object().author
        return self.request.user.is_superuser or self.request.user == author

    def get_success_url(self):
        return reverse_lazy('post_detail', args=[self.object.post.slug])
