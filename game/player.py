import random


# player class
class Player:
    # initialize
    # name: name of player
    # playerType: type of player (person or PC)
    def __init__(self, name, playerType=0):
        self.name = name
        self.playerType = playerType

        self.totalRolls = 0
        self.score = 0
        self.behaviourTypes = [["careful", 5, 20],
                               ["normal", 5, 7], ["aggressive", 5, 3]]

    # determines the behaviour of a PC player

    def makeDecision(self, number_of_rolls):
        behaviour = self.behaviourTypes[self.playerType - 1]

        number_of_y = ["y"] * behaviour[1]
        number_of_n = ["n"] * behaviour[2] * number_of_rolls
        choice_list = number_of_y + number_of_n
        choice = random.choice(choice_list)

        return choice
