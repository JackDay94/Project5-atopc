from django.test import TestCase
from checkout.forms import OrderForm


class TestCheckoutForms(TestCase):
    """Tests the checkout forms"""

    def test_order_form_valid_data(self):
        """Test the order form with valid data"""
        form = OrderForm(data={
            'full_name': 'test form',
            'email': 'test@test.com',
            'phone_number': '1234567890',
            'postcode': '123456',
            'town_or_city': 'any',
            'country': 'AF',
            'street_address1': 'any',
            'street_address2': 'any',
            'county': 'any',
        })

        self.assertTrue(form.is_valid())

    def test_order_form_no_data(self):
        """Test the order form with no data"""
        form = OrderForm(data={})

        self.assertFalse(form.is_valid())
