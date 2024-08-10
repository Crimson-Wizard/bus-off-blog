from django.contrib import admin
from .models import Media
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Media)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)