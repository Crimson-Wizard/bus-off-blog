from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


class CommentAdmin(SummernoteModelAdmin):
    list_display = ('post', 'author', 'approved')
    search_fields = ['approved']
    list_editable = ('approved',)
    
admin.site.register(Comment, CommentAdmin)
