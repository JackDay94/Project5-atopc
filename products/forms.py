from .models import Review, Product, Category
from django.forms import ModelForm
from django import forms
from .widgets import CustomClearableFileInput
from django_summernote.widgets import SummernoteWidget


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


class ProductForm(ModelForm):
    """
    Displays the product form.
    From CI Boutique Ado walkthrough.
    """
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('average_rating', 'wishlist',)
        widgets = {
            'description': SummernoteWidget(),
        }

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
