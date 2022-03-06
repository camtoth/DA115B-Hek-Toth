import unittest
import menu
import leaderboard as lb
import game


class TestMenuClass(unittest.TestCase):

    def setUp(self):
        self.menu = menu.Menu()

    def test_01_DefaultObject(self):
        # Instantiate an object and check its properties
        self.assertIsInstance(self.menu, menu.Menu)
        result_game = self.menu.new_game
        result_leaderboard = self.menu.leaderboard
        self.assertIsInstance(result_game, game.Game)
        self.assertIsInstance(result_leaderboard, lb.Leaderboard)