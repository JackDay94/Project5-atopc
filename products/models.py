from django.db import models
from django.contrib.auth.models import User

RATING = (
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
    rating = models.DecimalField(max_digits=6, decimal_places=1,
                                 null=True, blank=True, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    wishlist = models.ManyToManyField(User, blank=True, default=None,
                                      related_name='wishlist')

    def __str__(self):
        return self.name

    def update_product_rating(self):
        """
        Sets the rating for a product as an average of the ratings from reviews
        and sets the value to 0 if there is none
        """
        reviews = Review.objects.filter(product=self)
        self.rating = reviews.aggregate(models.Avg('rating'))['rating__avg']
        if self.rating is None:
            self.rating = 0
        self.save(update_fields=['rating'])


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
        ordering = ['-created_on']

    def __str__(self):
        return f"Product review for {self.product} by {self.author}"

    def save(self):
        super(Review, self).save()
        self.product.update_product_rating()
