import os
from django.core.asgi import get_asgi_application

"""
ASGI config for the busoff project.
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'busoff.settings')

application = get_asgi_application()
