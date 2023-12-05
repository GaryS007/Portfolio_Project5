from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Reviews(models.Model):
    """Defines the review model"""
    review_title = models.CharField(max_length=120)
    name = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    review_text = models.TextField(null=True, max_length=500)
    review_rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to="reviews_images/", null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Returns the full URL to the reviews route as a string"""
        return reverse("reviews")
    

