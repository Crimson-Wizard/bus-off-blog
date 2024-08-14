from django.shortcuts import render
from django.views.generic import ListView
from .models import Media

# Create your views here.


class MediaListView(ListView):
    model = Media
    template_name = 'media/media.html'
    context_object_name = 'media_list'

    def get_queryst(self):
        return Media.objects.all().order_by('-created_on')
