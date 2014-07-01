"""
WSGI config for convenient_delivery project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/convenient/Django/convenient_delivery/'
if path not in sys.path:
	sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "convenient_delivery.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#Appended for security
os.environ['HTTPS'] = "on"
