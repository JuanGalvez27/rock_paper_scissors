from django_apps.games.views import (
    GameCreateAPIView,
)
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("create/", GameCreateAPIView.as_view(), name="create_game"),
]
