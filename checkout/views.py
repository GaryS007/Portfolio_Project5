from django.shortcuts import render


def view_checkout(request):
    """ 
    A view to returns the products checkout page
    """

    return render(request, 'checkout/checkout.html')
