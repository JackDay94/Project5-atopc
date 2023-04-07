from django.test import TestCase
from newsletter.forms import NewsletterSignupForm


class TestNewsletterForm(TestCase):
    """Test the newsletter form"""

    def test_newsletter_form_valid_data(self):
        """Test the newsletter form with valid data"""
        form = NewsletterSignupForm(data={
            'full_name': 'test',
            'email_address': 'test@test.com',
        })

        self.assertTrue(form.is_valid())

    def test_newsletter_form_no_data(self):
        """Test the newsletter form with no data"""
        form = NewsletterSignupForm(data={})

        self.assertFalse(form.is_valid())
