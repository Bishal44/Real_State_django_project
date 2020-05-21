"""
Django settings for btre project.
"""

import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rd0yt^8sd!0_bk&*d3^x0tcv0wjbrv5+n^ws(2dum6zb(gh-q$'

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages.apps.PagesConfig',#from apps.py class
    'listings.apps.ListingsConfig',
    'realtors.apps.RealtorsConfig',
    'django.contrib.humanize',
    'accounts.apps.AccountsConfig',
    'contacts.apps.ContactsConfig',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'btre.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'btre.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
#

#for mysql
# 'ENGINE': 'django.db.backends.mysql',
#     'NAME': 'btre_db',
#     'USER': 'root',
#     'PASSWORD': 'root',
#     'HOST': "",
#     'PORT': "",
#     'OPTIONS': {
#     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btre_db',
        'USER':'postgres',
        'PASSWORD':'',
        'HOST':'localhost'
#         'ENGINE': 'django.db.backends.mysql',
#             'NAME': 'btre_db',
#             'USER': 'root',
#             'PASSWORD': 'root',
#             'HOST': "",
#             'PORT': "",
#             'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#
#
# }
}
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
#after running collectstatic collect all admin our static file at static folder


STATIC_ROOT=os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'btre/static')
]

#media folder setting
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'


#message
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',

}