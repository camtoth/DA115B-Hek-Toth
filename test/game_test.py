import unittest
from game.game import game


class TestGameClass(unittest.TestCase):
    def test_init_default_object(self):
        res = game.Game()
        exp = game.Game
        self.assertIsInstance(res, exp)


if __name__ == "__main__":
    unittest.main()
