from .base import *
from .secrets import *

DEBUG = True

INTERNAL_IPS = [
    '10.0.2.2',
]

INSTALLED_APPS += ('debug_toolbar',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}