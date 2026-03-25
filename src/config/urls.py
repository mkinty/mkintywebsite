from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Django
    path("admin/", admin.site.urls),

    # API
    # path("api/users/", include("apps.users.api.urls")),
    # path("api/auth/", include("apps.authentication.api.urls")),
    # path("api/notifications/", include("apps.notifications.api.urls")),
    # path("api/organizations/", include("apps.organizations.api.urls")),

    # Web (templates Django)
    path("", include("apps.home.web.urls", namespace="home")),
    path("users/", include("apps.users.web.urls", namespace="users")),
    path("auth/", include("apps.authentication.web.urls", namespace="auth")),
]

# Servir les fichiers media et statiques seulement en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
