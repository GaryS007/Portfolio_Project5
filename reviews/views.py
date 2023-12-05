from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Reviews
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def reviews(request):
    """ renders reviews page """

    list_reviews = (
        Reviews.objects.all().filter(approved=True).order_by("-updated_on"))
    return render(request, "reviews/reviews.html", {"list_reviews": list_reviews})
