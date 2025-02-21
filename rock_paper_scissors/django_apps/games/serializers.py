from django_apps.games.models import Game
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Game
        fields = "__all__"

    def set_winner(self, instance, winner):
        instance.winner = winner
        instance.save()
        return instance
