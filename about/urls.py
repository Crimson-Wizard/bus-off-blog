from . import views
from django.urls import path

"""
URL patterns for the about section of the website.
"""
urlpatterns = [
    path('', views.about_me, name='about'),
]
