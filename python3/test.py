from runner.koan import *
from koans.about_scoring_project import score
from koans.about_dice_project import DiceSet

class GreedPlayer:
#    def __init__(self):
    def __init__(self, playerid):
        self._id = playerid
        self._outcome = "undecided"
        self._score = None
        self.name = None

    @property
    def outcome(self):
        return self._outcome

    def create_player(self, name):
        self.name = name

class GreedGame:
    def __init__(self):
        self.players = list()

    def start_game(self, players = 2):

        prompt = "> "

        for playerid in ["player_{}".format(player) for player in range(1, players + 1)]:
            confirm = "n"
#            print(playerid)
            playerid = GreedPlayer(playerid)
            self.players.append(playerid)
#            print(playerid._id)
            while confirm != "y":
                print("Welcome to a game of Greed!. Please enter your name, {}".format(playerid._id))
                playerid.create_player(input(prompt))
                print("Hello, {}. Did I get that right? Are you ready to get greedy (y/n)?".format(playerid.name))
                confirm = input(prompt)
                if confirm == "y":
                    break

first_game = GreedGame()
first_game.start_game()
