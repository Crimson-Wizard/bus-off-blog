from django.contrib import admin
from .models import Gallery, GalleryForm
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Gallery)
class GalleryAdmin(SummernoteModelAdmin):
    """
    Admin interface configuration for the Gallery model.
    """
    form = GalleryForm
    list_display = ('title', 'created_on')
    search_fields = ['title']
    list_filter = ('created_on',)
    summernote_fields = ('content',)
