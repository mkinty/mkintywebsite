from src.apps.users.models import User


def create_user(email, password, username, first_name, last_name, avatar=None, bio=None):
    user = User.objects.create_user(
        email=email,
        password=password,
        username=username,
        first_name=first_name,
        last_name=last_name,
        avatar=avatar,
        bio=bio
    )
    return user


def update_user_profile(user, bio):
    user.bio = bio
    user.save()
    return user
