# Archvio de configuraciones comunes

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

# TODO Usar decouple para la SECRET_KEY
# Importamos config y la clase Csv de decouple, la cual lee los datos de los archivos env
# from decouple import config

# Se agrega un ".parent" mas ya que estamos dentro de una carpeta extra
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# TODO: usar decouple para sustraer la SECRET_KEY de un archivo env
SECRET_KEY = "django-insecure-cd)d@szix3vgh%vey_7ra1gr*x)#5g-=6mdy)*m9@vm@jxcky0"
# SECRET_KEY = config("SECRET_KEY", default="")

# Application definition
# Se divide INSTALLED_APPS en tres partes, las apps base, las apps locales que nosotrs creamos y las apps de terceros que podemos incorporar con pip install.
BASE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "apps.users",
    "apps.products",
    "apps.base",
]

THIRD_APPS = [
    "rest_framework",
    # Libreria para la autenticación por token
    "rest_framework.authtoken",
    # Libreria para simple history y rastrear las acciones del usuario
    "simple_history",
    # Esta libreria nos ayuda para la documentación con swagger
    'drf_yasg',
]

# Se juntan las tres partes en una sola variable
INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

ROOT_URLCONF = "dj_rest.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "dj_rest.wsgi.application"



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "es"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Colocamos la variable de entorno AUTH_USER_MODEL con nuestro modelo para usuarios personalizado
AUTH_USER_MODEL = "users.User"

TOKEN_EXPIRED_AFTER_SECONDS = 10