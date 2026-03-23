from django.db import models
from django.contrib.auth.models import AbstractUser
from markdownx.models import MarkdownxField


# Create your models here.


def user_profile_image_path(instance, filename):
    # Stocke les images dans media/users/<username>/<filename>
    return f'users/{instance.username}/{filename}'


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)  # optionnel
    last_name = models.CharField(max_length=30, blank=True)  # optionnel
    avatar = models.ImageField(
        upload_to=user_profile_image_path,
        null=True,
        blank=True
    )
    bio = MarkdownxField()  # <-- champ Markdown WYSIWYG

    def __str__(self):
        return self.username
