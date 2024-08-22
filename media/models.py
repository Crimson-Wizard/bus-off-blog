from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(default=datetime.now)
    featured_image = CloudinaryField('image')
    
    class Meta:
        ordering = ["-created_on"]


