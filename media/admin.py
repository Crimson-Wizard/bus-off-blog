from django.contrib import admin
from .models import Gallery
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Gallery)
# chnage about to gallery
class GalleryAdmin(SummernoteModelAdmin): 
    
    list_display = ('title', 'created_on')
    search_fields = ['title']
    list_filter = ('created_on',)
    summernote_fields = ('content',)