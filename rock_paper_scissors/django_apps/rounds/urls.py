from django_apps.rounds.views import RoundCreateAPIView, RoundRetrieveAPIView
from django.urls import path

urlpatterns = [
    path("create/", RoundCreateAPIView.as_view(), name="create_round"),
    path("by-game/<uuid:id>/", RoundRetrieveAPIView.as_view(), name="rouns_by_game"),
]
