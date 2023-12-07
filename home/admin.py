from django.contrib import admin
from .models import ContactUs
from djang_summernote.admin import SummernoteModelAdmin


@admin.regster(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """Represents the ContactUs model in the Django Admin Interface"""
    list_display = (__all)
    list_filter = ('sent_on')
    summernote_fields = ('message',)