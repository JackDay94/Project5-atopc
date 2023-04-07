from django.test import TestCase, Client
from django.urls import reverse


class TestHomeViews(TestCase):
    """Test the Home views"""

    def setUp(self):
        self.client = Client()

        self.home_url = reverse('home')
        self.about_us_url = reverse('about_us')
        self.privacy_policy_url = reverse('privacy_policy')

    def test_home_GET(self):
        """Test GET home view"""
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_about_us_GET(self):
        """Test GET about us view"""
        response = self.client.get(self.about_us_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')

    def test_post_list_GET(self):
        """Test GET privacy policy view"""
        response = self.client.get(self.privacy_policy_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/privacy_policy.html')
