from django_apps.players.views import PlayerAPIView
from django.urls import path

urlpatterns = [
    path("create/", PlayerAPIView.as_view(), name="create_player"),
    path("get/<uuid:id>/", PlayerAPIView.as_view(), name="get_player"),
]
