import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django_apps.games.models import Game
from django_apps.choices import MOVE_CHOICES
from django_apps.players.models import Player

class Round(models.Model):
    id = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        help_text="Round ID",
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    round_time = models.IntegerField()
    move_player_1 = models.SmallIntegerField(
        choices=MOVE_CHOICES, default=None, help_text="Player's move", null=True
    )
    move_player_2 = models.SmallIntegerField(
        choices=MOVE_CHOICES, default=None, help_text="Player's move", null=True
    )
    round_winner = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)
