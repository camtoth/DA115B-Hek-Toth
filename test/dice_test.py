import unittest
from game import dice


class TestDiceClass(unittest.TestCase):
    def test_init_default_object(self):
        res = dice.Dice()
        exp = dice.Dice
        self.assertIsInstance(res, exp)

    def test_dice_in_bound(self):
        diceroll = dice.Dice()
        rolls = diceroll.rollDice()
        for roll in rolls:
            res = roll
            exp = 1 <= res <= diceroll.numberOfSides
            self.assertTrue(exp)
