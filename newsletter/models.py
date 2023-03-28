from django.db import models


class NewsletterSignup(models.Model):
    """
    Model for newsletter signup.
    """
    full_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True, max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email_address
