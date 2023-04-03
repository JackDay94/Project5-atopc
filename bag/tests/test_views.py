from django.test import TestCase, Client
from django.urls import reverse


class TestBagViews(TestCase):
    """Test the bag views"""

    def test_view_bag_GET(self):
        client = Client()
        response = client.get(reverse('view_bag'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
