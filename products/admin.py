from django.contrib import admin
from .models import Product, Category, SpecialOffers
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """
    Displays the Product Model in the Admin Panel
    """
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "sale_price",
        "on_sale",
        "rating",
        "out_of_stock",
        "new_product",
        "special_offers",
        "b_stock",
    )
    summernote_fields = "description, product_dimensions, additional_description"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Displays the Category Model in the Admin Panel
    """
    list_display = (
        "friendly_name",
        "name",
    )

@admin.register(SpecialOffers)
class SpecialOffersAdmin(admin.ModelAdmin):
    """
    Displays the Special Offer Model in the admin panel
    """
    list_display = (
        "friendly_name",
        "name",
    )
