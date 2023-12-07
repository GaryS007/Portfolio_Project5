from django.contrib import admin
from .models import ContactUs
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """Represents the ContactUs model in the Django Admin Interface"""
    list_display = ('name', 'email', 'message', 'sent_on',)
    list_filter = ('sent_on',)
    summernote_fields = ('message',)