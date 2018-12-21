from itertools import cycle
from runner.koan import *
from koans.about_dice_project import DiceSet as DS
import pdb

class DiceSet(DS):
    def score(self):
    # You need to write this method
    #pass

# make the dice rolls into a dictionary counting up the number of each rolls' occurrences
        rolls = dict()
        for die in list(self._values):
            if not die in rolls:
                rolls[die] = 1
            else:
                rolls[die] += 1

# apply scoring rules to the dictionary of dice rolls
        total = 0
        unscored = 0
        if rolls == False:
            pass
        else:
            for die in rolls:
                if die == 1:
                    while rolls[die] >= 3: #for 3x1
                        total += 1000
                        rolls[die] -= 3
                    else:
                        total += rolls[die] * 100 #for remaining 1s
                elif die == 5:
                    while rolls[die] >= 3: #for 3x5
                        total += 500
                        rolls[die] -= 3
                    else:
                        total += rolls[die] * 50 #for remaining 5s
                else:
                    while rolls[die] >= 3: #for all other 3-of-a-kinds
                        total += die * 100
                        rolls[die] -= 3
                    else:
                        unscored += rolls[die]

        return (total, unscored)

class GreedPlayer:
#    def __init__(self):
    def __init__(self, playerid):
        self._id = playerid
        self._score = 0
        self._name = None
        self.had_final_turn = False
        self.in_the_game = False

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

class GreedGame:
    def __init__(self):
        self._players = list()
        self._num_players = 2
        self._turns = list()
        self._outcome = "undecided"

    @property
    def players(self):
        print("PLAYERS:")
        for player in range(self._num_players):
            print("Player {}: {}".format(player + 1, next(self._players).name))
        print("")
#        return self

    @property
    def score(self):
        print("SCORES")
        for player in range(self._num_players):
            pplayer = next(self._players)
            print("{}: {}".format(pplayer.name, pplayer.score))
        print("")

    @property
    def outcome(self):
        return self._outcome

    @outcome.setter
    def outcome(self, value):
        self._outcome = value

    def restart_game(self):
        print("Game restarting")
        self._turns = list()
        for player in range(self._num_players):
            reset_player = next(self._players)
            reset_player.score = 0
            reset_player.outcome = "undecided"
            reset_player.had_final_turn = False
            reset_player.in_the_game = False

# add the players to the game
    def initialize_players(self, players = 2):

        # since _players will be a cycle, we need to know the number of players in the game
        self._num_players = players
        prompt = "> "

        # run through the number of players and make a GreffPlayer for each, add to a list and set the name of the player
        for playerid in ["player_{}".format(player) for player in range(1, self._num_players + 1)]:
            #reset confirm input for each player
            confirm = "n"
#            print(playerid)
            playerid = GreedPlayer(playerid)
            self._players.append(playerid)
#            print(playerid._id)
            while confirm != "y":
                print("Welcome to a game of Greed!. Please enter your name, {}.".format(playerid._id))
                playerid.name = input(prompt)
                print("Hello, {}. Did I get that right? Are you ready to get greedy (y/n)?".format(playerid.name))
                confirm = input(prompt)
                if confirm == "y":
                    break

        print("The game of Greed is ready to be played between with {} players. When you're ready, start the game.\n".format(len(self._players)))
        # set the players as a cycle
        self._players = cycle(self._players)

    def start_game(self):

        prompt = "> "
        confirm = None

        #condition if it's the first turn
        if len(self._turns) == 0:
            print("Round 1 begins! (Remember you need to score at least 300 points in a single turn before your scores will be added to the total)\n")
            self.next_turn()
        #restart condition, because game is already in progress
        else:
            while confirm != "y":
                print("Are you sure you want to start a new game, you will lose {} turns (y/n)?".format(len(self._turns)))
                confirm = input(prompt)
                if confirm == "y":
                    self.restart_game()
                    break
                if confirm == "n":
                    print("Keep playing your current game with 'next_turn()'\n")
                    break

    def next_turn(self):

        prompt = "> "
        confirm = None
        num_roll = 5

        current_turn = Turn("{}".format(len(self._turns) + 1), next(self._players))
        self._turns.append(current_turn)

        if current_turn._player.had_final_turn == True:
            self.end_game()
            return

        print("{}, you're up!".format(current_turn._player.name))
        if current_turn._player.in_the_game == False:
            print("Remember you need to score at least 300 points before scores will be added to your total")

        while confirm != "n":
            current_turn.diceroll.roll(num_roll)
            roll_score, unscored_dice = current_turn.diceroll.score()
            current_turn._score += roll_score
            print("\nYou rolled {}. This is worth {} points for a total of {} points this turn".format(current_turn.diceroll.values, roll_score, current_turn._score))

            if roll_score == 0:
                print("Sorry you didn't score on this roll and so your turn is over. Use 'next_turn()' to continue the game\n")
                break

            if unscored_dice == 0 and len(current_turn.diceroll.values) == 5:
                unscored_dice == 5

            print("You can roll up to {} dice again to add to your score. Feeling greedy (y/n)?".format(unscored_dice))
            confirm = input(prompt)
            if confirm == "y":
                num_roll = unscored_dice
            if confirm == "n":

                if current_turn._player.in_the_game == False and current_turn._score < 300:
                    print("Playing it safe? Remember you need to score at least 300 points to 'get in the game'\n")
                    break
                else:
                    current_turn._player.in_the_game = True
                    current_turn._player._score += current_turn._score

                if current_turn._player._score >= 3000:
                    print("You have over 3000 points. This is your last turn. Please let the other's know the next turn is their last\n")
                    current_turn._player.had_final_turn = True

                print("{} scored {} points this turn. Their total points are: {}. Keep playing with 'next_turn()'\n".format(current_turn._player.name, current_turn._score, current_turn._player.score))
                break

    def end_game(self):
        print("GAME OVER\n")
        ranks = list()
        for player in range(self._num_players):
            pplayer = next(self._players)
            ranks.append((pplayer, pplayer.score))
        ranks.sort(key=lambda tup: tup[1], reverse=True)

        self.outcome = "{} wins!\n".format(ranks[0][0].name)
        print(self.outcome)

        print("RANKING:")
        for player, score in ranks:
            print("{}: {}".format(player.name, score))

class Turn():
    def __init__(self, turnid, player):
        self._turn_id = turnid
        self._player = player
        self.diceroll = DiceSet()
        self._score = 0

first_game = GreedGame()
first_game.initialize_players()
first_game.players
first_game.score
first_game.start_game()
