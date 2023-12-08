from .models import ContactUs
from django import forms


class ContactUsForm(forms.ModelForm):
    """ Creates field for ContactEnquiry form """
    class Meta:
        model = ContactUs
        fields = ('__all__')
        """
        Labels replace the default labels for forms.
        """
