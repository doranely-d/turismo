# -*- coding: utf-8 -*-
import datetime
import os
DEBUG = True

DEFAULT_FROM_EMAIL = 'Nombre <correo@dominio.com>'
SITE_NAME = 'SITE NAME'
DOMAIN_NAME = 'http://domain.com'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# SMTP Settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'correo@dominio.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# FACEBOOK
FACEBOOK_GRAPH_URL = 'https://graph.facebook.com/oauth/access_token'
# INSTAGRAM
INSTAGRAM_GRAPH_URL = 'https://api.instagram.com/v1/users/self/media/recent/?access_token={0}'

# Google Maps Api Key
GEOPOSITION_GOOGLE_MAPS_API_KEY = ''

# Databases
  # SQL Database
USE_SQLITE = True

if not USE_SQLITE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '',  # Database Name
            'USER': '',  # Database User
            'PASSWORD': '',  # Database User Password
            'OPTIONS': {'charset': 'utf8mb4'},
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }

# Server Config
ADMINS = (
    #('Nombre', 'correo@dominio.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = []

# Only for production Mode for apache to serve static and media files
# MEDIA_ROOT = os.path.join()
# MEDIA_URL = ''
# STATIC_ROOT = os.path.join()
# STATIC_URL = ''
