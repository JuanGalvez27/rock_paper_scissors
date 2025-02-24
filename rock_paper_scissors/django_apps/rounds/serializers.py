from datetime import timezone

from django_apps.choices import MOVE_CHOICES
from django_apps.games.models import Game
from django_apps.rounds.models import Round
from django_apps.utils import RockPaperScissors
from rest_framework import serializers


class RoundSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    game = serializers.UUIDField()
    round_time = serializers.IntegerField()
    move_player_1 = serializers.ChoiceField(choices=MOVE_CHOICES)
    move_player_2 = serializers.ChoiceField(choices=MOVE_CHOICES)
    round_winner = serializers.UUIDField(read_only=True)

    class Meta:
        model = Round
        fields = [
            "id",
            "game",
            "round_time",
            "move_player_1",
            "move_player_2",
            "round_winner",
        ]

    def create(self, validated_data):
        try:
            game = Game.objects.get(id=validated_data["game"])
        except Game.DoesNotExist:
            raise serializers.ValidationError("Game does not exist")
        validated_data["game"] = game
        rock_paper_scissors = RockPaperScissors()
        winner = rock_paper_scissors.set_winner(
            validated_data["move_player_1"], validated_data["move_player_2"]
        )
        validated_data["round_winner"] = None
        if winner == 1:
            validated_data["round_winner"] = game.player1
        elif winner == 2:
            validated_data["round_winner"] = game.player2

        return Round.objects.create(**validated_data)
