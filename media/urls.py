# from . import views
from .views import GalleryListView
from django.urls import path

urlpatterns = [
    path('',  GalleryListView.as_view(), name='gallery-list'),
]

