import django_heroku

from .base import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

django_heroku.settings(locals())
