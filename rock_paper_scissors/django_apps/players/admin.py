from django_apps.players.models import Player
from django.contrib import admin


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass