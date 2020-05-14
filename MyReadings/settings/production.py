import django_heroku

from .base import *

DEBUG = False

# Activate Django-Heroku.
django_heroku.settings(locals())
