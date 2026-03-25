from django.shortcuts import render, redirect

from apps.authentication.services.auth_service import register_user
from .forms import RegisterForm


def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        print("form is valid", form.cleaned_data)
        register_user(form.cleaned_data)

        return redirect("home:home-page")

    return render(
        request,
        "authentication/register.html",
        {"form": form}
    )


def login_view(request):

    return render(
        request,
        "authentication/login.html"
    )
