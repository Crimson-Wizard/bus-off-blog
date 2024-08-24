from django.views.generic import ListView
from .models import Gallery

# Create your views here.


class GalleryListView(ListView):
    """
    View to list all galleries on the gallery page
    **Context**
    ``Gallery``
        the most recent instance of :model:`media.Gallery`.
    
    **Template**
    :template: `media/gallery.html`
    """
    model = Gallery
    template_name = 'media/gallery.html'
    context_object_name = 'gallery_list'

    def get_queryst(self):
        """
        Return all galleries ordered by creation date.
        """
        return Gallery.objects.all().order_by('-created_on')
