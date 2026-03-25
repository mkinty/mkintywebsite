from django import forms
from apps.users.models import User


class RegisterForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={
        "id": "bio-editor",  # id pour Quill
        "class": "form-control",
        "placeholder": "Votre bio"
    }), required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name", "avatar", "bio"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Votre prénom"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Votre nom"}),
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Votre pseudo"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Votre email"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Votre mot de passe"}),
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


