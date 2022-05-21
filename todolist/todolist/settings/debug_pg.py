from .debug import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ToDo',
        'USER': 'maksr',
        'PASSWORD': 'qwerty',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}