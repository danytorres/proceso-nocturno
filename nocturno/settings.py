"""
Django settings for nocturno project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import environ
import os
from botocore.config import Config

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, 'secure/.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'corsheaders',
    "procesos",
    'django_extensions',
    "graphene_django",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "nocturno.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "procesos/template",
            BASE_DIR / "nocturno/template"
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "nocturno.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # "default": {
    #    "ENGINE": "django.db.backends.sqlite3",
    #    "NAME": BASE_DIR / "db.sqlite3",
    # },
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'xaldigital',
        'USER': env('POSTGRESUSER'),
        'PASSWORD': env('POSTGRESPSSW'),
        'HOST': env('POSTGRESHOST'),
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Mexico_City"

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

GRAPHENE = {
    "SCHEMA": "nocturno.schema.schema"
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
]

S3_LOCATION = "s3://eph-datalake-dev-utilities/logs"

my_config = Config(
    region_name="us-east-1",
)

CONFIG_DATA_AWS = {
    "access": env("ACCESS_KEY_AWS"),
    "secret": env("SECRET_KEY_AWS"),
    "location": S3_LOCATION,
    "config": my_config,
    "query": "",
}

ssh_key_pem = os.path.join(BASE_DIR, 'secure/palaciokey.pem')

ssh_server = "ec2-18-213-16-147.compute-1.amazonaws.com"

LOGIN_REDIRECT_URL = '/'

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
