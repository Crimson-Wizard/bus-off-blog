from django.contrib import admin
from .models import Media
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Media)
class AboutAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'created_on')
    search_fields = ['title']
    list_filter = ('created_on',)
    summernote_fields = ('content',)