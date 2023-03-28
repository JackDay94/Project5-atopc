from django.forms import ModelForm
from .models import NewsletterSignup


class NewsletterSignup(ModelForm):
    """
    Displays the Newsletter signup form.
    """
    model = NewsletterSignup
    exclude = ('date_added',)
