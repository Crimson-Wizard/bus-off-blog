from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField


class Gallery(models.Model):
    """
    Model representing a gallery with images and descriptions.
    """
    title = models.CharField(max_length=100)
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(default=datetime.now)
    featured_image = CloudinaryField('image')

    class Meta:
        ordering = ["-created_on"]
