from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/players/", include("django_apps.players.urls")),
    path("api/games/", include("django_apps.games.urls")),
    path("api/rounds/", include("django_apps.rounds.urls")),
]
