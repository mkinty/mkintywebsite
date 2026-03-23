from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST", "db"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}

# Media files
MEDIA_URL = os.getenv("MEDIA_URL", "/media/")
MEDIA_ROOT = os.getenv("MEDIA_ROOT", BASE_DIR / "media")

# Static files
STATIC_URL = os.getenv("STATIC_URL", "/static/")
STATICFILES_DIRS = [
    BASE_DIR / "static",  # pointe vers src/static si BASE_DIR = src/
]
STATIC_ROOT = os.getenv("STATIC_ROOT", BASE_DIR / "staticfiles")

# URL du broker et du backend pour Celery
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND")