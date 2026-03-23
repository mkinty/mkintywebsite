from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="home"),  # si vue fonctionnelle
    path("", views.HomePageView.as_view(), name="home"),  # si CBV
]
