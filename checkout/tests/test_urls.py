from django.test import SimpleTestCase
from django.urls import resolve, reverse
from checkout.views import cache_checkout_data, checkout, checkout_success
from checkout.webhooks import webhook


class TestCheckoutUrls(SimpleTestCase):
    """Tests the checkout urls"""

    def test_checkout_url_resolves(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)

    def test_cache_checkout_data_url_resolves(self):
        url = reverse('cache_checkout_data')
        self.assertEquals(resolve(url).func, cache_checkout_data)

    def test_checkout_success_url_resolves(self):
        url = reverse('checkout_success', args=['123'])
        self.assertEquals(resolve(url).func, checkout_success)

    def test_webhook_url_resolves(self):
        url = reverse('webhook')
        self.assertEquals(resolve(url).func, webhook)
