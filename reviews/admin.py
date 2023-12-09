from django.contrib import admin
from .models import Reviews
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Reviews)
class ReviewsAdmin(SummernoteModelAdmin):
    """Displays reviews in django admin"""
    list_display = (
        "name",
        "review_name",
        "review_title",
        "updated_on",
        "review_rating",
        "approved",
    )
    summernote_fields = "review_text"

    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        """
        Adds approval action to drop-down list
        """
        queryset.update(approved=True)

