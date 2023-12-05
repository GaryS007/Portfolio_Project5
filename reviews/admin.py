from django.contrib import admin
from .models import Reviews


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Displays reviews in django admin"""
    list_display = (
        "name",
        "review_title",
        "updated_on",
        "review_text",
        "review_rating",
        "approved",
    )
