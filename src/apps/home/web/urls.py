from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    # path("", views.index, name="home"),  # si vue fonctionnelle
    path("", views.HomePageView.as_view(), name="home-page"),  # si CBV
]
