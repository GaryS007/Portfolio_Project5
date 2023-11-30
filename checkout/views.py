from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NviWUAz6g5uj61Kfy7eWEsUUC0PbBJlw2wy75T4MVCdI1vdXBRjlijfv26cbm2U9fdScfQyCQ4T0aX6xDu9LC5I00xJRjsiMz',
        'client_secret': 'client_test_secret',
    }

    return render(request, template, context)