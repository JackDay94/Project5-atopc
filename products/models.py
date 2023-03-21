from django.db import models
from django.contrib.auth.models import User


RATING = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

class Category(models.Model):
    """Category model (from CI Boutique Ado Walkthrough)"""
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """Product model (from CI Boutique Ado walkthrough)"""
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    average_rating = models.DecimalField(max_digits=6, decimal_places=1,
                                         null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    specification = models.TextField()

    def __str__(self):
        return self.name

    def update_review_fields(self):
        """
        Updates the average_star field depending on average user rating.
        Taken from:
        https://www.reddit.com/r/django/comments/kp6rz4/which_is_the_proper_way_of_calculating_average/
        """
        reviews = self.reviews.all()
        self.rating = reviews.aggregate(models.Avg('average_rating')).get(
            'rating__avg'
            )
        self.save(update_fields=['average_rating'])


class Review(models.Model):
    """Review model for user product reviews"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews')
    rating = models.IntegerField(choices=RATING, default=0)
    review_content = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Product review for {self.product} by {self.author}"

    def save(self, *args, **kwargs):
        """
        Overwrites the save method in Review and calls update_review_fields
        method after saving the object.
        Taken from:
        https://www.reddit.com/r/django/comments/kp6rz4/which_is_the_proper_way_of_calculating_average/
        """
        super(Review, self).save(*args, **kwargs)
        self.product.update_review_fields()
