from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from .models import ContactUs
from .forms import ContactUsForm
from django.contrib import messages


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
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            message = request.POST['message']
            subject = request.POST['subject']
            email = request.POST['email']
            form.save()
            messages.success(request, 'Message successfully submitted')
            return redirect(reverse('contact'))
            try:
                send_mail(
                    subject=subject,
                    message=message,
                    # Customer's Email
                    from_email=email,
                    # Send to email
                    recipient_list=['chattomeh@hotmail.com'],
                )
                send_mail(
                    subject='Drum Loot Contact Enquiry',
                    message='Thank you for your email\
                        Someone will be in touch with you soon.',
                    from_email=email,
                )
            except ImportError:
                message.error(request, 'There was an error sending your message.')
        else:
            messages.error(request, 'Failed to submit message. Please ensure the form is valid. ')
    else:
        form = ContactUsForm()

    form = ContactUsForm()
    template = 'home/contact_us.html'
    context = {'form': form}

    return render(request, template, context)