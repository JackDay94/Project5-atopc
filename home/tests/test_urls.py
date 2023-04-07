from django.test import SimpleTestCase
from django.urls import resolve, reverse
from home.views import HomeView, about, privacy_policy


class TestHomeUrls(SimpleTestCase):
    """Test the Home urls"""

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_about_url_resolves(self):
        url = reverse('about_us')
        self.assertEquals(resolve(url).func, about)

    def test_privacy_policy_url_resolves(self):
        url = reverse('privacy_policy')
        self.assertEquals(resolve(url).func, privacy_policy)
