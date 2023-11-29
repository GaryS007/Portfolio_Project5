from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

def view_checkout(request):
    """ 
    A view to returns the products checkout page
    """

    return render(request, 'checkout/checkout.html')


def add_to_checkout(request, item_id):
    """ 
    Add a quantity of the specified product to the shopping cart
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}.')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart.')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_checkout(request, item_id):
    """ 
    Adjust the quantity of the specified product in the shopping cart
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_checkout'))


def remove_from_checkout(request, item_id):
    """ 
    Remove item from checkout
    """

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
            messages.error(request, f'Error removing item: {e}')
            return HttpResponse(status=500)
