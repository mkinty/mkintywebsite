from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Accueil"
        context["message"] = "Bienvenue sur la page d'accueil de notre site !"
        return context
