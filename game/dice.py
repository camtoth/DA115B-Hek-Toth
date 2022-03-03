import random


# dice class
class Dice:
    # initialize class
    # numberOfDice: the number of dice in a roll, defaults to 1
    # numberOfSides: the number of sides of a dice, defaults to 6
    def __init__(self, numberOfDice=1, numberOfSides=6):
        self.numberOfDice = numberOfDice
        self.numberOfSides = numberOfSides

    # rolls the dice/die and returns the result
    def rollDice(self):
        rolls = []

        for dice in range(0, self.numberOfDice):
            roll = random.randint(1, self.numberOfSides)
            rolls.append(roll)

        return rolls
