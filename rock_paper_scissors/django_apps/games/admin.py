from django_apps.games.models import Game
from django.contrib import admin


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
