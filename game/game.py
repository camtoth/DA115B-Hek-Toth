import random
import time
import dice
import player as pl


# game class
class Game:
    # initialize
    # players: list of players in the game
    # turn: current turn number
    # active: boolean if game is active of not
    def __init__(self, players=[], maxPlayers=2, gameSpeed=1, maxScore=100):
        self.players = players
        self.maxPlayers = maxPlayers
        self.gameSpeed = gameSpeed
        self.maxScore = maxScore

        self.active = True
        self.turn = 0

    def output(self, text, duration=1):
        time.sleep(duration / self.gameSpeed)
        print(text)

    def chooseRules(self):
        self.output("CHOOSE RULES")
        self.output("1: 1 die", 0)
        self.output("2: 2 dice", 0)

        choice = 0
        while choice == 0:
            try:
                choice = int(input("Your choice:"))
                if choice == 1:
                    self.rules = "1 die"
                    self.dice = dice.Dice()
                elif choice == 2:
                    self.rules = "2 dice"
                    self.dice = dice.Dice(2, 6)
                else:
                    choice = 0
            except BaseException:
                pass

        self.output("Great, let's play a game with" + str(self.rules) + "!")

    def choosePlayers(self):
        choice = -1
        while (len(self.players) < self.maxPlayers):
            print("")
            self.output("CHOOSE PLAYER" + str(len(self.players) + 1))
            self.output("1: Human Player", 0)
            self.output("2: PC Player", 0)

            try:
                choice = int(input("Your choice: "))

                # real player
                if choice == 1:
                    name = input("Your name: ")
                    playerType = 0
                    player = pl.Player(name=name, playerType=playerType)
                    self.players.append(player)

                # computer player
                elif choice == 2:
                    playerName = "PC" + str(len(self.players) + 1)
                    self.output("computer is called " + playerName)
                    player = pl.Player(name=playerName)

                    self.output("Choose playing style")
                    choices = []
                    for i, btype in enumerate(player.behaviourTypes):
                        print(str(i + 1) + ":", btype[0])
                        choices.append(i + 1)

                    choice2 = 0
                    while choice2 not in choices:
                        try:
                            choice2 = int(input("Your choice:"))
                        except BaseException:
                            pass

                    player.playerType = choice2
                    self.players.append(player)
            except BaseException:
                pass

        print("")
        self.output("There are " +
                    str(len(self.players)) +
                    " players in the game")
        print("")

    # method initiates a new game

    def setupGame(self):
        self.output("Welcome to the game of PIG!")
        print("")
        self.output("The rules are simple,")
        self.output("each player takes turns throwing 1 or 2 dice.")
        self.output("A player can roll an unlimited number of times" +
                    "in one turn.")
        self.output("When ending a turn all roll results are" +
                    "added to the total score.")
        self.output("The first player reaching " +
                    str(self.maxScore) + " wins.")
        self.output("Some special rules:")
        self.output("- When rolling a double, the player" +
                    "is forced to roll again.")
        self.output(
            "- When rolling a 1, the player's points of that turn" +
            "are lost.")
        self.output("- When rolling double 1, all of the player's" +
                    "points are lost.")
        self.output("")

        self.chooseRules()
        self.choosePlayers()

    # method to show the current score of all players

    def showScore(self):
        for i in range(0, len(self.players)):
            self.output(self.players[i].name + " has " +
                        str(self.players[i].score) + " points")
        print("")

    # method to handle the actions of a player

    def playerAction(self, player):
        temp_score = 0
        action = ""
        number_of_rolls = 0

        while action != "n":

            if action == "y2":
                action = "y"
            else:
                # human player
                if player.playerType == 0:
                    action = input("Throw dice? (y/n)")

                # pc player
                else:
                    print("computer is thinking...")
                    action = player.makeDecision(number_of_rolls)

                    if action == "y":
                        self.output("computer throws dice", 3)
                    else:
                        self.output("computer ends turn", 3)

            # dice is rolled
            if action == "y":
                player.totalRolls += 1
                result = self.dice.rollDice()
                temp_score += sum(result)

                self.output("You roll " +
                            str(result[0]) +
                            " and " +
                            str(result[1]) +
                            " (" +
                            str(temp_score) +
                            " points this turn)")

                if 1 in result:
                    temp_score = 0
                    action = "n"
                    self.output("you role a 1!")

                # more than one die is thrown
                if len(result) > 0:
                    similar = True
                    for i in range(1, len(result)):
                        if result[i] != result[i - 1]:
                            similar = False
                            break

                    # players rolls same numbers
                    if similar:
                        # players throws all 1's
                        if result[i] == 1:
                            player.score = 0
                            temp_score = 0
                            self.output("snake eyes!")
                        # player will need to throw again
                        else:
                            action = "y2"
                            self.output("same numbers!")
            elif action == "end":
                action = "n"
                temp_score = self.maxScore
                self.output("player magically rolls " + str(self.maxScore))

            number_of_rolls += 1

            if (action != "y2") and (
                    (player.score + temp_score) >= self.maxScore):
                action == "n"

        # add new results to total score
        player.score += temp_score

        self.output(player.name + "'s turn ends")
        self.output("gained " +
                    str(temp_score) +
                    " points, with new total " +
                    str(player.score))

    # method runs a game

    def runGame(self):
        self.output("Lets play a game!")

        random.shuffle(self.players)
        self.output("Player " + self.players[0].name + " starts...")

        # loop while game is active
        while self.active:
            # Process a turn
            self.turn += 1
            print("")
            self.output("--- TURN " + str(self.turn) + "---", 2)
            self.showScore()

            # loop through all players
            for player in self.players:
                print("")
                self.output(
                    player.name + " active (current score "
                    + str(player.score) + ")")
                self.playerAction(player)

                if player.score >= self.maxScore:
                    print(
                        self.maxScore,
                        "reached!",
                        player.name,
                        "wins the game!")
                    self.active = False
                    break

        print("")
        self.output("the game has ended")
