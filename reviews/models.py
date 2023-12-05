from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Reviews(models.Model):
    """Defines the review model"""
    class Meta:
        verbose_name_plural = "Reviews"

    review_title = models.CharField(max_length=120)
    name = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    review_text = models.TextField(null=True, max_length=500)
    review_rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)],
        null=True)
    image = models.ImageField(upload_to="reviews_images/", null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Returns the full URL to the reviews route as a string"""
        return reverse("reviews")
    

