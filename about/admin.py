from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    About admin configuration
    """
    summernote_fields = ('content',)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(SummernoteModelAdmin):
    """
    CollaborateRequest admin configuration
    """
    summernote_fields = ('message',)
    list_display = ('name', 'read',)
    summernote_fields = ('content',)