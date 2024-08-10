from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Media(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField("photo")
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(default=datetime.now)
