from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration for the Blog application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
