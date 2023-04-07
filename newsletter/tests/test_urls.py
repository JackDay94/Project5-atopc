from django.test import SimpleTestCase
from django.urls import resolve, reverse
from newsletter.views import newsletter


class TestNewsletterUrls(SimpleTestCase):
    """Tests the newsletter urls"""

    def test_newsletter_url_resolves(self):
        url = reverse('newsletter')
        self.assertEquals(resolve(url).func, newsletter)
