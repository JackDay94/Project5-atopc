from django.test import SimpleTestCase
from django.urls import resolve, reverse
from blog.views import (
    PostList,
    PostDetail,
    AddPost,
    EditPost,
    DeletePost,
    EditComment,
    DeleteComment)


class TestBlogUrls(SimpleTestCase):
    """Test urls for the Blog"""

    def test_blog_url_resolves(self):
        url = reverse('blog')
        self.assertEquals(resolve(url).func.view_class, PostList)

    def test_post_detail_url_resolves(self):
        url = reverse('post_detail', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, PostDetail)

    def test_add_post_url_resolves(self):
        url = reverse('add_post')
        self.assertEquals(resolve(url).func.view_class, AddPost)

    def test_edit_post_url_resolves(self):
        url = reverse('edit_post', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, EditPost)

    def test_delete_post_url_resolves(self):
        url = reverse('delete_post', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, DeletePost)

    def test_edit_comment_url_resolves(self):
        url = reverse('edit_comment', args=[1])
        self.assertEquals(resolve(url).func.view_class, EditComment)

    def test_delete_comment_url_resolves(self):
        url = reverse('delete_comment', args=[1])
        self.assertEquals(resolve(url).func.view_class, DeleteComment)
