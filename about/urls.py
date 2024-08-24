from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_me, name='about'),
    """URL patterns for the about section of the website."""
]
