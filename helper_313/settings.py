"""
Django settings for helper_313 project (Render-ready).
"""

from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# SECURITY SETTINGS
# -----------------------------
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 
    'django-insecure-38%c2bhjj@061tlo48c)l1cho&*q06b5&k63o3p%&werib3_1h'
)

# DEBUG mode (use False on production)
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Allowed hosts (comma-separated in env variable)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# -----------------------------
# INSTALLED APPS
# -----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Your apps
    'helper_313.events',
    'helper_313.profiles',
    'helper_313.projects',
    'helper_313.programs',
    'helper_313.courses',
    
    # Third-party apps
    'corsheaders',
    'rest_framework',
]

# -----------------------------
# MIDDLEWARE
# -----------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'helper_313.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'helper_313.wsgi.application'

# -----------------------------
# DATABASE (Postgres via DATABASE_URL)
# -----------------------------
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

# -----------------------------
# PASSWORD VALIDATION
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------
# INTERNATIONALIZATION
# -----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------------
# STATIC FILES
# -----------------------------
STATIC_URL = '/static/'

# For Render, collectstatic will place files in STATIC_ROOT
STATIC_ROOT = BASE_DIR / 'staticfiles'

# -----------------------------
# CORS SETTINGS
# -----------------------------
CORS_ALLOW_ALL_ORIGINS = True

# -----------------------------
# DEFAULT AUTO FIELD
# -----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'