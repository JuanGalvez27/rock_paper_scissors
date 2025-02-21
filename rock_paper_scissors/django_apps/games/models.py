import uuid

from django.db import models
from django_apps.players.models import Player


class Game(models.Model):
    id = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        help_text="Game ID",
    )
    player1 = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="games_as_player1"
    )
    player2 = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="games_as_player2"
    )
    winner = models.ForeignKey(
        Player, on_delete=models.CASCADE, null=True, related_name="games_as_winner"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
