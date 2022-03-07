import random


class Player:
    '''
    Player class that models a user in the game
    Attributes:
    name (str): name of player
    playerType (int): type of player (person=0 or PC=1..3)
    '''

    def __init__(self, name="", playerType=0):
        '''
        constructor of player class
        standard start attributes:
        totalRolls (int): total rolls made in the game (starts at 0)
        score (int): the current score of the player (starts at 0)
        behaviourTypes (list): list of behaviourtypes of a PC player.
                               [description,number of 'y', number of 'n']
        '''

        self.name = name
        self.playerType = playerType

        self.totalRolls = 0
        self.score = 0
        self.behaviourTypes = [["careful", 5, 20],
                               ["normal", 5, 7], ["aggressive", 5, 3]]

    def makeDecision(self, number_of_rolls):
        '''
        Method that determines if a PC player rolls a dice or ends his turn.
        A choice list is made containing 'y' and 'n' characters.
        The starting number of 'y'/'n' is determined by the behaviourType.
        The number of 'n' increases with each number of rolls in a turn.
        The increase of 'n' is based on the behaviourtype.
        With the random module a value is selected from the choice list,
        'y' player makes a roll or 'n' player ends his turn.

        Parameters:
        number_of_rolls (int): current number of rolls made in a turn.
        '''

        behaviour = self.behaviourTypes[self.playerType - 1]

        number_of_y = ["y"] * behaviour[1]
        number_of_n = ["n"] * behaviour[2] * number_of_rolls
        choice_list = number_of_y + number_of_n
        choice = random.choice(choice_list)

        return choice
