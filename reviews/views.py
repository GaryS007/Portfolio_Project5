from django.shortcuts import render
from .models import Reviews


def reviews(request):
    """ renders reviews page """

    list_reviews = (
        Reviews.objects.all().filter(approved=True).order_by("-updated_on"))
    return render(request, "reviews/reviews.html", {"list_reviews": list_reviews})
