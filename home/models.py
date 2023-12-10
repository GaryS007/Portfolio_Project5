""" Models for Contact """
from django.db import models


class ContactUs(models.Model):
    """ Defines the Contact Us Model """
    class Meta:
        """ Plural Name for Django Admin """
        verbose_name_plural = "Contact Us"
    name = models.CharField(max_length=80, blank=True)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=60, blank=True)
    message = models.TextField(blank=True)
    sent_on = models.DateTimeField(auto_now_add=True, null=True)
