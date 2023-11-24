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
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    product_dimensions = models.TextField(blank=True)
    additional_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    previous_price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to="product_images/", null=True, blank=True)
    out_of_stock = models.BooleanField(default=False)
    new_product = models.BooleanField(default=False)
    special_offers = models.ForeignKey(
        "SpecialOffers", null="True", blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name
