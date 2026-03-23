# Structure globale du projet
___
```Plain text
project/
│
├── docker/
├── docker-compose.yml
├── .env.dev
├── .env.prod
│
├── src/
│
│   ├── config/
│   │   ├── settings/
│   │   │   ├── base.py
│   │   │   ├── dev.py
│   │   │   └── prod.py
│   │   ├── urls.py
│   │   └── wsgi.py
│
│   ├── apps/
│   │
│   │   ├── users/
│   │   └── authentication/
│
│   ├── templates/
│   └── static/
│
└── manage.py
```

## App users

**Responsabilité :**

- modèle utilisateur
- profil
- gestion des utilisateurs

**Structure**

```Plain text
apps/users/
│
├── admin.py
├── apps.py
├── models.py
├── migrations/
│
├── selectors/
│   └── user_selectors.py
│
├── services/
│   └── user_services.py
│
├── web/
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
└── tests/
```

**models.py**

```Python
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
```

**selectors/user_selectors.py**

Les selectors servent uniquement à lire la base de données.

```Python
from apps.users.models import User


def get_user_by_id(user_id: int):
    return User.objects.filter(id=user_id).first()


def get_all_users():
    return User.objects.all()


def get_user_by_email(email: str):
    return User.objects.filter(email=email).first()
```

**services/user_services.py**

Les services contiennent la logique métier.

```Python
from django.contrib.auth import get_user_model

User = get_user_model()


def create_user(email, password, username):
    user = User.objects.create_user(
        email=email,
        password=password,
        username=username
    )
    return user


def update_user_profile(user, bio):
    user.bio = bio
    user.save()
    return user
```

**web/views.py**

```Python
from django.shortcuts import render
from apps.users.selectors.user_selectors import get_all_users


def user_list_view(request):
    users = get_all_users()

    return render(
        request,
        "users/user_list.html",
        {"users": users}
    )
```

**web/urls.py**

```Python
from django.urls import path
from .views import user_list_view

urlpatterns = [
    path("", user_list_view, name="user_list"),
]
```

## App authentication

**Responsabilité :**

- login
- logout
- register
- reset password

**Structure**

```Plain text
apps/authentication/
│
├── apps.py
├── admin.py
│
├── selectors/
│   └── auth_selectors.py
│
├── services/
│   └── auth_services.py
│
├── web/
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
└── tests/
```

**web/forms.py**

```Python
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "username", "password"]
        
```

**services/auth_services.py**

```Python
from django.contrib.auth import authenticate, login
from apps.users.services.user_services import create_user


def register_user(data):
    user = create_user(
        email=data["email"],
        password=data["password"],
        username=data["username"]
    )
    return user


def login_user(request, email, password):

    user = authenticate(
        request,
        email=email,
        password=password
    )

    if user:
        login(request, user)

    return user
```

**web/views.py**

```Python
from django.shortcuts import render, redirect
from .forms import RegisterForm
from apps.authentication.services.auth_services import register_user


def register_view(request):

    form = RegisterForm(request.POST or None)

    if form.is_valid():

        register_user(form.cleaned_data)

        return redirect("login")

    return render(
        request,
        "auth/register.html",
        {"form": form}
    )
```

**web/urls.py**

```Python
from django.urls import path
from .views import register_view

urlpatterns = [
    path("register/", register_view, name="register"),
]
```

### Ajout dans urls principal

```Python
from django.urls import path, include

urlpatterns = [
    path("users/", include("apps.users.web.urls")),
    path("auth/", include("apps.authentication.web.urls")),
]
```

### Avantages de cette architecture

- séparation logique métier / requêtes / vues
- code testable
- facile à faire évoluer
- structure utilisée dans les gros projets Django

### Structure finale d'une app moderne

```Plain text
app/
│
├── models.py
├── admin.py
│
├── selectors/     ← requêtes DB
├── services/      ← logique métier
├── web/
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
└── tests/
```