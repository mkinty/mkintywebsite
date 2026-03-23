from src.apps.users.models import User


def get_user_by_id(user_id: int):
    return User.objects.filter(id=user_id).first()


def get_all_users():
    return User.objects.all()


def get_user_by_email(email: str):
    return User.objects.filter(email=email).first()
