from .views import GalleryListView
from django.urls import path

"""
URL patterns for the Gallery application.
"""
urlpatterns = [
    path('',  GalleryListView.as_view(), name='gallery-list'),
]
