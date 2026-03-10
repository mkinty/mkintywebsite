from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


def user_profile_image_path(instance, filename):
    # Stocke les images dans media/users/<username>/<filename>
    return f'users/{instance.username}/{filename}'


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)  # optionnel
    last_name = models.CharField(max_length=30, blank=True)  # optionnel
    profile_image = models.ImageField(
        upload_to=user_profile_image_path,
        null=True,
        blank=True
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
