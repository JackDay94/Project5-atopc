from django.test import TestCase
from blog.forms import BlogPostForm, BlogCommentForm


class TestBlogForms(TestCase):
    """Test the blog forms"""
    def test_blog_post_form_valid_data(self):
        """Test the blog post form with valid data"""
        form = BlogPostForm(data={
            'title': 'post1',
            'subtitle': 'post1',
            'post_content': 'test',
            'image_url': '',
            'blog_image': '',
            'status': 1,
        })

        self.assertTrue(form.is_valid())

    def test_blog_post_form_no_data(self):
        """Test the blog post form with no data"""
        form = BlogPostForm(data={})

        self.assertFalse(form.is_valid())

    def test_blog_comment_form_valid_data(self):
        """Test the blog comment form with valid data"""
        form = BlogCommentForm(data={
            'content': 'test',
        })

        self.assertTrue(form.is_valid())

    def test_blog_comment_form_no_data(self):
        """Test the blog comment form with no data"""
        form = BlogCommentForm(data={})

        self.assertFalse(form.is_valid())
