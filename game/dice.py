import random


# dice class
class Dice:
    '''
    Class that models the dice in the game.
    '''
    def __init__(self, numberOfDice=1, numberOfSides=6):
        '''
        Constructor of the dice class
        Attributes:
        numberofDice (int): number of dice in a roll (standard value = 1).
        numberofSides (int): number of sides of a dice (standard value = 6).
        '''

        self.numberOfDice = numberOfDice
        self.numberOfSides = numberOfSides

    def rollDice(self):
        '''
        Method rolls the dice and returns the result in a int list.
        '''
        rolls = []

        for dice in range(0, self.numberOfDice):
            roll = random.randint(1, self.numberOfSides)
            rolls.append(roll)

        return rolls
