from frameable.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../frameable.sqlite3'),
    }
}

try:
    from website.settings.dev_local import *
except ImportError:
    pass
