from .models import Review
from django.forms import ModelForm


class ReviewForm(ModelForm):
    """
    Displays the review form.
    """
    class Meta:
        model = Review
        fields = (
            "rating",
            "review_content",
        )
