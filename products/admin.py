from django.contrib import admin
from .models import Product, Category
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
        "previous_price",
        "rating",
        "out_of_stock",
        "new_product",
    )
    summernote_fields = "description"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Displays the Category Model in the Admin Panel
    """
    list_display = (
        "friendly_name",
        "name",
    )
