import uuid
from django.db import models


class Category(models.Model):
    """
    Model for Categories
    """
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class SpecialOffers(models.Model):
    """
    Model for Special Offers
    """

    class Meta:
        verbose_name_plural = "Special Offers"

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """Model for Products"""
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    product_dimensions = models.TextField(blank=True)
    additional_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to="product_images/", null=True, blank=True)
    # Product Sales
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    out_of_stock = models.BooleanField(default=False)
    new_product = models.BooleanField(default=False)
    special_offers = models.ForeignKey(
        'SpecialOffers', null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    def _generate_sku(self):
        """Generate a random, unique SKU using UUID"""
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the SKU number
        if it hasn't been set already.
        """
        if not self.sku:
            self.sku = self._generate_sku()
        super().save(*args, **kwargs)
