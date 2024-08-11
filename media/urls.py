from . import views
from .views import MediaListView
from django.urls import path

urlpatterns = [
    path('',  MediaListView.as_view(), name='media-list'),
]

