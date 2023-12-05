from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Reviews
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ReviewsForm


def reviews(request):
    """ renders reviews page """

    list_reviews = (
        Reviews.objects.all().filter(approved=True).order_by("-updated_on"))
    return render(request, "reviews/reviews.html", {"list_reviews": list_reviews})

@login_required
def add_review(request):
    """ Add a review to the reviews page """
    if not request.user:
        messages.error(request, 'Sorry, you must login to do that.')
        return redirect(reverse('reviews'))

    if request.method == 'POST':
        form = ReviewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            review = form.save()
            messages.success(request, 'Successfully posted a review, waiting for approval.')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        form = ReviewsForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_review(request, pk):
    """ Edit an existing review """
    if not request.user:
        messages.error(request, 'Sorry, you must login to do that.')
        return redirect(reverse('reviews'))
    
    review = get_object_or_404(Reviews, id=pk)
    if request.method == 'POST':
        form = ReviewsForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your review, waiting for approval.')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Failed to update your review. Please ensure the form is valid.')
    else:
        form = ReviewsForm(instance=review)

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)