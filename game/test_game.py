# unittesting of game class
import io
import unittest
from unittest import mock
import game
import player
import dice


class TestGameClass(unittest.TestCase):
    def setUp(self):
        self.game = game.Game()

    def test_01_DefaultObject(self):
        # Instantiate an object and check its properties
        self.assertIsInstance(self.game, game.Game)

        result = self.game.maxPlayers
        expected = 2
        self.assertEqual(result, expected)

        result = self.game.gameSpeed
        expected = 1
        self.assertEqual(result, expected)

        result = self.game.maxScore
        expected = 100
        self.assertEqual(result, expected)

    @mock.patch('game.input', create=True)
    def test_02_ChooseRules2(self, mocked_input):
        # test choice of rules 2 dice game
        mocked_input.side_effect = ['2']
        self.game.chooseRules()

        result = self.game.dice.numberOfDice
        expected = 2
        self.assertEqual(result, expected)

    @mock.patch('game.input', create=True)
    def test_03_ChooseRules2(self, mocked_input):
        # test choice of rules 1 dice game
        mocked_input.side_effect = ['1']
        self.game.chooseRules()

        result = self.game.dice.numberOfDice
        expected = 1
        self.assertEqual(result, expected)

    @mock.patch('game.input', create=True)
    def test_04_ChoosePlayers(self, mocked_input):
        # test player selection
        mocked_input.side_effect = ['1', 'Kalle', '2', '1']
        self.game.choosePlayers()

        # check correct number of players
        result = len(self.game.players)
        expected = 2
        self.assertEqual(result, expected)

        # check player1 name
        result = self.game.players[0].name
        expected = 'Kalle'
        self.assertEqual(result, expected)

        # check player1 type
        result = self.game.players[0].playerType
        expected = 0
        self.assertEqual(result, expected)

        # check player2 name
        result = self.game.players[1].name
        expected = 'PC2'
        self.assertEqual(result, expected)

        # check player1 type
        result = self.game.players[1].playerType
        expected = 1
        self.assertEqual(result, expected)

    def test_05_ChangeName(self):
        # tests name change functionality

        # test name change player 1
        nameChange = "Jenny"
        self.game.changeName(nameChange, 1)

        result = self.game.players[0].name
        self.assertEqual(result, nameChange)

        # test name change player 2
        nameChange = "Olaf"
        self.game.changeName(nameChange, 2)

        result = self.game.players[1].name
        self.assertEqual(result, nameChange)

    @mock.patch('game.input', create=True)
    def test_06_PlayerAction1(self, mocked_input):
        # test player input
        mocked_input.side_effect = ['n']

        self.game.playerAction(self.game.players[0])

        result = self.game.players[0].score

        self.assertEqual(result, 0)

    def test_07_PlayerAction2(self):
        # test player input
        initialScore = self.game.players[1].score
        initialRolls = self.game.players[1].totalRolls

        self.game.dice = dice.Dice()
        self.game.playerAction(self.game.players[1])

        newScore = self.game.players[1].score
        newRolls = self.game.players[1].totalRolls
        result = newScore - initialScore
        rolls = newRolls - initialRolls

        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 6 * rolls)

    @mock.patch('builtins.print')
    def test_08_Output(self, mock_print):
        # check if print output corresponds with input
        self.game.output("hello world")
        mock_print.assert_called_with("hello world")

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_09_ShowScore(self, mock_out):
        # check if correct scores are printed
        self.game.players[0].score = 50
        self.game.players[1].score = 51
        self.game.players[0].name = "Tanja"
        self.game.players[1].name = "Kristof"

        self.game.showScore()

        self.assertEqual(
            mock_out.getvalue(),
            "Tanja has 50 points\nKristof has 51 points\n\n")


if __name__ == "__main__":
    unittest.main()
