#!/usr/bin/env python
# -*- coding: utf-8 -*-

# EXTRA CREDIT:
#
# Create a program that will play the Greed Game.
# Rules for the game are in GREED_RULES.TXT.
#
# You already have a DiceSet class and score function you can use.
# Write a player class and a Game class to complete the project.  This
# is a free form assignment, so approach it however you desire.

from runner.koan import *
from about_scoring_project import score
from about_dice_project import DiceSet

class GreedPlayer:
    def __init__(self):
        self.name = None

class GreedGame:
    def __init__(self):
        self.players = list()

    def start_game(self, players = 2):

        prompt = "> "
        confrim = "n"

        for playerid in ["player_{}".format(player) for player in range(1, players)]:
            playerid = GreedPlayer()
            while confrim != "y":
                print("Welcome {} to a game of Greed!. Please enter your name".format(playerid))
                playerid.name = input(prompt)
                print("Hello, {}. Did I get that right? Are you ready to get greedy?".format(playerid.name))
                if confirm == "y":
                    break

class AboutExtraCredit(Koan):
    # Write tests here. If you need extra test classes add them to the
    # test suite in runner/path_to_enlightenment.py
    def test_extra_credit_task(self):
        pass

    def test_players_can_be_created_and_edited(self):
        player1 = GreedPlayer()

# Play a game of greed