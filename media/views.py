from django.shortcuts import render
from .models import Media

# Create your views here.

def media_detail(request):
    
    media = Media.objects.all().order_by('-created_on').first()
    
    return render(
        request,
        "media/media.html",
        {"media": media,}
    )