from django_apps.rounds.models import Round
from django.contrib import admin


@admin.register(Round)
class RoundAdmin(admin.ModelAdmin):
    pass
