from runner.koan import *
from koans.about_scoring_project import score
from koans.about_dice_project import DiceSet

class GreedPlayer:
    def __init__(self):
        self.name = None
        self.id = None

class GreedGame:
    def __init__(self):
        self.players = list()

    def start_game(self, players = 2):

        prompt = "> "

        for playerid in ["player_{}".format(player) for player in range(1, players + 1)]:
            confirm = "n"
            print(dir(playerid))
            playerid = GreedPlayer()
            print(dir(playerid))
            while confirm != "y":
                print("Welcome to a game of Greed!. Please enter your name, {}".format(playerid))
                playerid.name = input(prompt)
                print("Hello, {}. Did I get that right? Are you ready to get greedy (y/n)?".format(playerid.name))
                confirm = input(prompt)
                if confirm == "y":
                    break

GreedGame().start_game()
