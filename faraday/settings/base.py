from django.contrib import messages

from unipath import Path
PROJECT_DIR = Path(__file__).ancestor(3)

SECRET_KEY = '=+t8w&x0y*!yzpyy1i@m!@!g%%cfxx^byq_7&s5i8f#7llg60v'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'turnstile',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'faraday.urls'
WSGI_APPLICATION = 'faraday.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'EST'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

MEDIA_ROOT = PROJECT_DIR.child("uploads")
MEDIA_URL = '/uploads/'

LOGIN_URL = 'turnstile_login'

MESSAGE_TAGS = {
    messages.constants.ERROR: 'danger'    # Fix up for Bootstrap.
}
