from django.contrib.auth import authenticate, login

from apps.users.services.user_service import create_user


def register_user(data):
    user = create_user(
        email=data["email"],
        password=data["password"],
        username=data["username"],
        first_name=data["first_name"],
        last_name=data["last_name"],
        avatar=data["avatar"],
        bio=data["bio"]

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
