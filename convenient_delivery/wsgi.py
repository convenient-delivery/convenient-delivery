"""
WSGI config for convenient_delivery project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "convenient_delivery.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
