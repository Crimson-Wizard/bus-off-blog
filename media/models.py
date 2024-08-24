from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField
from django import forms
# from django.contrib import admin


class Gallery(models.Model):
    """
    Model representing a gallery with images and descriptions.
    stores list of images stored on cloudinary 
    """
    title = models.CharField(max_length=100)
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(default=datetime.now)
    featured_image = CloudinaryField('image only')

    class Meta:
        ordering = ["-created_on"]


class GalleryForm(forms.ModelForm):
    """
    Validates form to ensure only images files can be uploaded 
    returns error message "Only image files are allowed."
    """
    class Meta:
        model = Gallery
        fields = '__all__'
        
    def clean_featured_image(self):
        """
        Validates that the uploaded file for the featured_image field is an image.
        
        Raises:
            forms.ValidationError: If the uploaded file is not an image.
        
        Returns:
            The cleaned data for the featured_image field if valid.
        """
        featured_image = self.cleaned_data.get('featured_image')

        if featured_image:
            if not featured_image.content_type.startswith('image/'):
                raise forms.ValidationError("Only image files are allowed.")
        
        return featured_image
