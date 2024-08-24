import os
"""
WSGI config for the busoff project.
"""
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'busoff.settings')

application = get_wsgi_application()
