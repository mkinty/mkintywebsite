import os
from celery import Celery

# définir le settings Django
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    os.getenv("DJANGO_SETTINGS_MODULE", "config.settings.local"),
)

# créer l'application celery
app = Celery("mkwebsite")

# charger la configuration depuis Django settings
app.config_from_object("django.conf:settings", namespace="CELERY")

# détecter automatiquement les fichiers tasks.py
app.autodiscover_tasks()
