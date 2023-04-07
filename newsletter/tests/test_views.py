from django.test import TestCase, Client
from django.urls import reverse
from newsletter.models import NewsletterSignup


class TestNewsletterViews(TestCase):
    """Tests the newsletter views"""

    def setUp(self):
        self.client = Client()

        self.signup1 = NewsletterSignup.objects.create(
            full_name='Test',
            email_address='test@test.com',
        )

        self.newsletter_url = reverse('newsletter')

    def test_newsletter_GET(self):
        """Test GET newsletter view"""
        response = self.client.get(self.newsletter_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter/newsletter.html')
