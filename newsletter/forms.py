from django.forms import ModelForm
from .models import NewsletterSignup


class NewsletterSignupForm(ModelForm):
    """
    Displays the Newsletter signup form.
    """
    class Meta:
        model = NewsletterSignup
        exclude = ('date_added',)
