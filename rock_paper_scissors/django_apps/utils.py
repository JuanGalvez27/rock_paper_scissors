from django.urls import reverse
from django_apps.choices import move_choices_dict


def view_url(view, keyword_args={}):
    url = "http://testserver" + reverse(view, kwargs=keyword_args)
    return url


class RockPaperScissors:

    GAME_RULES = {
        move_choices_dict["Rock"]: move_choices_dict["Scissors"],
        move_choices_dict["Paper"]: move_choices_dict["Rock"],
        move_choices_dict["Scissors"]: move_choices_dict["Paper"],
    }

    def set_winner(self, move_player_1, move_player_2):
        """
        Determine the winner of the game.

        :param move_player_1: Player 1 move ("Rock", "Paper", "Scissors")
        :param move_player_2: Player 2 move ("Rock", "Paper", "Scissors")
        :return: 1 if player 1 wins, 2 if player 2 wins, None if there is a tie.
        """
        if move_player_1 == move_player_2:
            return None

        return 1 if self.GAME_RULES[move_player_1] == move_player_2 else 2
