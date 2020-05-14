from .base import *

DEBUG = True

SECRET_KEY = 'w%&j=$w6t6%$+rn!kf4^*14*&&&!n2)hao1e2b+_jwv-r%b*66'

INSTALLED_APPS += [
    'debug_toolbar',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INTERNAL_IPS = [
    '10.0.2.2',
]
