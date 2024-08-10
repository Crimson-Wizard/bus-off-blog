from . import views
from django.urls import path

urlpatterns = [
    path('', views.media_detail, name='media'),
]

