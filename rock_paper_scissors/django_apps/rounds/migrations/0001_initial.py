# Generated by Django 5.0.8 on 2025-02-21 01:31

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Round ID', primary_key=True, serialize=False, unique=True)),
                ('round_time', models.IntegerField()),
                ('move_player_1', models.SmallIntegerField(choices=[(1, 'Rock'), (2, 'Paper'), (3, 'Scissors')], default=None, help_text="Player's move", null=True)),
                ('move_player_2', models.SmallIntegerField(choices=[(1, 'Rock'), (2, 'Paper'), (3, 'Scissors')], default=None, help_text="Player's move", null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game')),
                ('round_winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.player')),
            ],
        ),
    ]
