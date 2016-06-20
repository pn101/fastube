import os
from .base import PROJECT_ROOT_DIR
from .base import BASE_DIR


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'fastube', 'static',)]

STATIC_URL = '/static/'

# Media Files
MEDIA_ROOT = os.path.join(
        PROJECT_ROOT_DIR,
        'dist',
        'media',
)

MEDIA_URL = '/media/'
