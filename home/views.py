from django.shortcuts import render
from .models import ContactUs


# Create your views here.

def index(request):
    """ 
    A view to return the index page 
    """
    return render(request, 'home/index.html')


def contact_us(request):
    """ 
    Handles the logic for the contact form
    """
    if request.method == "POST":
        form = ContactUsForm(request.POST)
    else:
        return render(request, 'home/contact_us.html')