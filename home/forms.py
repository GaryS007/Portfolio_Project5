from .models import ContactUs
from django import forms


class ContactUsForm(forms.ModelForm):
    """ Creates field for ContactEnquiry form """
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'subject', 'message',)
        """
        Labels replace the default labels for forms.
        """
