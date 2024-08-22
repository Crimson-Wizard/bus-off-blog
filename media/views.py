from django.views.generic import ListView
from .models import Gallery

# Create your views here.

class GalleryListView(ListView):
    model = Gallery
    template_name = 'media/gallery.html'
    context_object_name = 'gallery_list'

    def get_queryst(self):
        return Gallery.objects.all().order_by('-created_on')
