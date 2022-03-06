# unittesting of dice class
import unittest
import dice


class Test_01_DiceClass(unittest.TestCase):
    def setUp(self):
        self.dice = dice.Dice()

    def test_01_DefaultObject(self):
        # Instantiate an object and check its properties
        self.assertIsInstance(self.dice, dice.Dice)

        result = self.dice.numberOfSides
        expected = 6
        self.assertEqual(result, expected)

        result = self.dice.numberOfDice
        expected = 1
        self.assertEqual(result, expected)

    def test_02_RollResult1Dice(self):
        # Roll one dice and check value is in bounds
        roll = self.dice.rollDice()
        roll_result = sum(roll)
        result = 1 <= roll_result <= self.dice.numberOfSides
        self.assertTrue(result)

        # Roll two die and check value is in bounds
        self.dice.numberOfDice = 2
        roll = self.dice.rollDice()
        roll_result = sum(roll)
        result = 2 <= roll_result <= (self.dice.numberOfSides * 2)
        self.assertTrue(result)

    def test_03_NumberOfDice1(self):
        # check if dice roll has the correct number of dice
        self.dice.numberOfDice = 1
        roll = self.dice.rollDice()
        result = len(roll)
        expected = 1

        self.assertEqual(result, expected)

    def test_04_NumberOfDice2(self):
        # check if dice roll has the correct number of dice
        self.dice.numberOfDice = 2
        roll = self.dice.rollDice()
        result = len(roll)
        expected = 2

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
