from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField

# Create your models here.

class Media(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media-img/')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(default=datetime.now)
    featured_image = CloudinaryField('image', default='placeholder')
    
    class Meta:
        ordering = ["-created_on"]


