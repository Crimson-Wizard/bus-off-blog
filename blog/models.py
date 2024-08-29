from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django import forms


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Model representing a blog post.
    Stores a single comment post entry related to :model:'auth.User'.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

class PostForm(forms.ModelForm):
    """
    Form for the Post model that validates the uploaded file to ensure
    that only image files can be used as the featured image.

    Raises:
        forms.ValidationError: If the uploaded file is not an image.
    """
    class Meta:
        model = Post
        fields = '__all__'

def clean_featured_image(self):
    """
    Validates that the uploaded file for the featured_image field is an image.
    If no image is uploaded, it sets a placeholder image URL.
    
    Raises:
        forms.ValidationError: If the uploaded file is not an image.
    
    Returns:
        The cleaned data for the featured_image field if valid, or the placeholder image URL.
    """
    featured_image = self.cleaned_data.get('featured_image')

    # URL of the placeholder image
    placeholder_image_url = 'https://res.cloudinary.com/dx4vjg39s/image/upload/v1724866922/pondering_marqxn.jpg'

    if isinstance(featured_image, str):
        # If featured_image is a string (e.g., URL or path), we assume it's valid
        if "placeholder" in featured_image:
            return placeholder_image_url
        return featured_image
    
    if featured_image:
        if not featured_image.content_type.startswith('image/'):
            raise forms.ValidationError("Only image files are allowed.")
    else:
        # No image uploaded, use the placeholder image URL
        return placeholder_image_url

    return featured_image


class Comment(models.Model):
    """
    Model representing a comment on a blog post.
    Stores a single comment post entry related to :model:'auth.User'
    and  :model:'blog.Post'.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.body} | written by {self.author}"
