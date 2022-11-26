# Archivo de configuraciones especificas para entorno local

# Importamos todo el contenido de base.py el cual contiene las caracteristicas comunes
# tanto para entorno local como para producción
from .base import *

# Importamos config y la clase Csv de decouple, la cual lee los datos de los archivos env
from decouple import Csv, config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool, default=True)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=list, default=[])

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"


