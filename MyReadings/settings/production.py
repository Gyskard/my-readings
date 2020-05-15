import django_heroku

from .base import *

DEBUG = False

SECRET_KEY = 'w%&j=$w6t6%$+rn!kf4^*14*&&&!n2)hao1e2b+_jwv-r%b*66'

django_heroku.settings(locals())
