from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import BlogPost, BlogComment


class TestBlogViews(TestCase):
    """Test the blog views"""

    def setUp(self):
        self.client = Client()

        self.post1 = BlogPost.objects.create(
            title='post1',
            slug='post1',
            status=1,
        )

        self.comment1 = BlogComment.objects.create(
            author=User.objects.create_user(
                username='test',
                email='test@test.com', password='test'
                ),
            post=self.post1,
            content='testing',
        )

        self.blog_url = reverse('blog')
        self.detail_url = reverse('post_detail', args=['post1'])
        self.add_post_url = reverse('add_post')
        self.edit_post_url = reverse('edit_post', args=['post1'])
        self.delete_post_url = reverse('delete_post', args=['post1'])
        self.edit_comment_url = reverse('edit_comment', args=[1])
        self.delete_comment_url = reverse('delete_comment', args=[1])

    def test_post_list_GET(self):
        """Test GET post list view"""
        response = self.client.get(self.blog_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_post_detail_GET(self):
        """Test GET post detail view"""
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_detail.html')

    def test_add_post_user_is_superuser_GET(self):
        """Test GET add post view for logged in superuser"""
        User.objects.create_superuser(
            username='admin',
            email='admin@test.com', password='admintest'
        )
        self.client.login(
            username='admin',
            email='admin@test.com', password='admintest'
        )

        response = self.client.get(self.add_post_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add_post.html')

    def test_add_post_user_not_superuser_GET(self):
        """Test GET add post view for logged in user"""
        self.client.login(
            username='test',
            email='test@test.com', password='test'
        )

        response = self.client.get(self.add_post_url)

        self.assertEquals(response.status_code, 403)
        self.assertTemplateUsed(response, 'errors/403.html')

    def test_add_post_user_not_authenticated_GET(self):
        """Test GET add post view for unauthenticated user"""
        self.client.logout()

        response = self.client.get(self.add_post_url)

        self.assertEquals(response.status_code, 302)

    def test_edit_post_user_is_superuser_GET(self):
        """Test GET edit post view for logged in superuser"""
        User.objects.create_superuser(
            username='admin',
            email='admin@test.com', password='admintest'
        )
        self.client.login(
            username='admin',
            email='admin@test.com', password='admintest'
        )

        response = self.client.get(self.edit_post_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_post.html')

    def test_edit_post_user_not_superuser_GET(self):
        """Test GET edit post view for logged in user"""
        self.client.login(
            username='test',
            email='test@test.com', password='test'
        )

        response = self.client.get(self.edit_post_url)

        self.assertEquals(response.status_code, 403)
        self.assertTemplateUsed(response, 'errors/403.html')

    def test_edit_post_user_not_authenticated_GET(self):
        """Test GET edit post view for unauthenticated user"""
        self.client.logout()

        response = self.client.get(self.edit_post_url)

        self.assertEquals(response.status_code, 302)

    def test_delete_post_user_is_superuser_GET(self):
        """Test GET delete post view for logged in superuser"""
        User.objects.create_superuser(
            username='admin',
            email='admin@test.com', password='admintest'
        )
        self.client.login(
            username='admin',
            email='admin@test.com', password='admintest'
        )

        response = self.client.get(self.delete_post_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/delete_post.html')

    def test_delete_post_user_not_superuser_GET(self):
        """Test GET delete post view for logged in user"""
        self.client.login(
            username='test',
            email='test@test.com', password='test'
        )

        response = self.client.get(self.delete_post_url)

        self.assertEquals(response.status_code, 403)
        self.assertTemplateUsed(response, 'errors/403.html')

    def test_delete_post_user_not_authenticated_GET(self):
        """Test GET delete post view for unauthenticated user"""
        self.client.logout()

        response = self.client.get(self.delete_post_url)

        self.assertEquals(response.status_code, 302)

    def test_edit_comment_user_is_superuser_GET(self):
        """Test GET edit comment view for logged in superuser"""
        User.objects.create_superuser(
            username='admin',
            email='admin@test.com', password='admintest'
        )
        self.client.login(
            username='admin',
            email='admin@test.com', password='admintest'
        )

        response = self.client.get(self.edit_comment_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_comment.html')

    def test_edit_comment_user_not_superuser_GET(self):
        """Test GET edit comment view for logged in user"""
        self.client.login(
            username='test',
            email='test@test.com', password='test'
        )

        response = self.client.get(self.edit_comment_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_comment.html')

    def test_edit_comment_user_not_author_GET(self):
        """
        Test GET edit comment view for logged in user that is not the
        comment author
        """
        User.objects.create_user(
            username='test2',
            email='test2@test.com', password='test2'
        )
        self.client.login(
            username='test2',
            email='test2@test.com', password='test2'
        )

        response = self.client.get(self.edit_comment_url)

        self.assertEquals(response.status_code, 403)
        self.assertTemplateUsed(response, 'errors/403.html')

    def test_edit_comment_user_not_authenticated_GET(self):
        """Test GET edit comment view for unauthenticated user"""
        self.client.logout()

        response = self.client.get(self.edit_comment_url)

        self.assertEquals(response.status_code, 302)

    def test_delete_comment_user_is_superuser_GET(self):
        """Test GET delete comment view for logged in superuser"""
        User.objects.create_superuser(
            username='admin',
            email='admin@test.com', password='admintest'
        )
        self.client.login(
            username='admin',
            email='admin@test.com', password='admintest'
        )

        response = self.client.get(self.delete_comment_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/delete_comment.html')

    def test_delete_comment_user_not_superuser_GET(self):
        """Test GET delete comment view for logged in user"""
        self.client.login(
            username='test',
            email='test@test.com', password='test'
        )

        response = self.client.get(self.delete_comment_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/delete_comment.html')

    def test_delete_comment_user_not_author_GET(self):
        """
        Test GET delete comment view for logged in user that is not the
        comment author
        """
        User.objects.create_user(
            username='test2',
            email='test2@test.com', password='test2'
        )
        self.client.login(
            username='test2',
            email='test2@test.com', password='test2'
        )

        response = self.client.get(self.delete_comment_url)

        self.assertEquals(response.status_code, 403)
        self.assertTemplateUsed(response, 'errors/403.html')

    def test_delete_comment_user_not_authenticated_GET(self):
        """Test GET delete comment view for unauthenticated user"""
        self.client.logout()

        response = self.client.get(self.delete_comment_url)

        self.assertEquals(response.status_code, 302)
