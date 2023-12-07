from django.db import models


class ContactUs(models.Model):
    """ Defines the Contact Us Model """
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=80, blank=True)
    message = models.TextField(blank=True)
    subject = models.CharField(max_length=60, blank=True)
    sent_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
