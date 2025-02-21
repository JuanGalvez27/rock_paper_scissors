from django_apps.players.models import Player
from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=60)

    class Meta:
        model = Player
        fields = ["id", "name"]