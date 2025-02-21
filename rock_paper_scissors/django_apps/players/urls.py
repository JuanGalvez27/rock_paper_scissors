from django_apps.players.views import PlayerCreateAPIView, PlayerRetrieveAPIView
from django.urls import path

urlpatterns = [
    path("create/", PlayerCreateAPIView.as_view(), name="create_player"),
    path("get/<uuid:id>/", PlayerRetrieveAPIView.as_view(), name="get_player"),
]
