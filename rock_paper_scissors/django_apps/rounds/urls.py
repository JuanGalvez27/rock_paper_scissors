from django_apps.rounds.views import RoundCreateAPIView
from django.urls import path

urlpatterns = [
    path("create/", RoundCreateAPIView.as_view(), name="create_round"),
]
