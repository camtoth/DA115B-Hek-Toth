# unittesting of game class
import io
import unittest
from unittest import mock
import game
import dice
import player as pl
import leaderboard as lb


class TestGameClass(unittest.TestCase):
    '''
    Unittesting of game class.
    '''
    def setUp(self):
        '''Create game class.'''
        self.leaderboard = lb.Leaderboard()
        self.game = game.Game(self.leaderboard)
        self.game.gameSpeed = 10

    def test_01_DefaultObject(self):
        '''Instantiate an object and check its properties.'''
        self.assertIsInstance(self.game, game.Game)

        result = self.game.maxPlayers
        expected = 2
        self.assertEqual(result, expected)

        result = self.game.gameSpeed
        expected = 10
        self.assertEqual(result, expected)

        result = self.game.maxScore
        expected = 50
        self.assertEqual(result, expected)

    @mock.patch('game.input', create=True)
    def test_02_ChooseRules2(self, mocked_input):
        '''Test choice of rules 2 dice game.'''
        mocked_input.side_effect = ['2']
        self.game.chooseRules()

        result = self.game.dice.numberOfDice
        expected = 2
        self.assertEqual(result, expected)

    @mock.patch('game.input', create=True)
    def test_03_ChooseRules2(self, mocked_input):
        '''Test choice of rules 1 dice game.'''
        mocked_input.side_effect = ['1']
        self.game.chooseRules()

        result = self.game.dice.numberOfDice
        expected = 1
        self.assertEqual(result, expected)

    @mock.patch('game.input', create=True)
    def test_04_ChooseRules3(self, mocked_input):
        '''Test choice of rules when wrong input.'''
        mocked_input.side_effect = ['wwww', '1']
        self.game.chooseRules()

        result = self.game.dice.numberOfDice
        expected = 1
        self.assertEqual(result, expected)

    @mock.patch('game.input', create=True)
    def test_05_ChoosePlayers(self, mocked_input):
        '''Test player selection.'''
        mocked_input.side_effect = ['www', '1', 'Kalle', '2', 'www', '1']
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

    def test_06_ChangeName(self):
        '''Tests name change functionality.'''

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
    def test_07_PlayerAction1(self, mocked_input):
        '''Test player input.'''
        mocked_input.side_effect = ['n']

        self.game.playerAction(self.game.players[0])

        result = self.game.players[0].score

        self.assertEqual(result, 0)

    def test_08_PlayerAction2(self):
        '''Test player input.'''
        initialScore = self.game.players[1].score
        initialRolls = self.game.players[1].totalRolls

        self.game.dice = dice.Dice(2, 6)
        self.game.playerAction(self.game.players[1])

        newScore = self.game.players[1].score
        newRolls = self.game.players[1].totalRolls
        result = newScore - initialScore
        rolls = newRolls - initialRolls

        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 12 * rolls)

    @mock.patch('builtins.print')
    def test_09_Output(self, mock_print):
        '''Check if print output corresponds with input.'''
        self.game.output("hello world")
        mock_print.assert_called_with("hello world")

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_10_ShowScore(self, mock_out):
        '''Check if correct scores are printed.'''
        self.game.players[0].score = 50
        self.game.players[1].score = 51
        self.game.players[0].name = "Tanja"
        self.game.players[1].name = "Kristof"

        self.game.showScore()

        self.assertEqual(
            mock_out.getvalue(),
            "Tanja has 50 points\nKristof has 51 points\n\n")

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_11_ShowRules(self, mock_out):
        '''Check if rules are printed.'''

        l1 = "\nWelcome to the game of PIG!\n"
        l2 = "\n"
        l3 = "The rules are simple,\n"
        l4 = "each player takes turns throwing 1 or 2 dice.\n"
        l5 = "A player can roll an unlimited number of times in one turn.\n"
        l6 = "When ending a turn all roll results are "
        l7 = "added to the total score.\n"
        l8 = "The first player reaching 50 wins.\n"
        l9 = "Some special rules:\n"
        l10 = "- When rolling a double, the player is "
        l11 = "forced to roll again.\n"
        l12 = "- When rolling a 1, the player's points of "
        l13 = "that turn are lost.\n"
        l14 = "- When rolling double 1, all of the player's points are lost.\n"
        l15 = "\n"

        txt1 = l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8
        txt2 = l9 + l10 + l11 + l12 + l13 + l14 + l15

        self.game.showRules()
        self.assertEqual(mock_out.getvalue(), txt1+txt2+"\n")

    @mock.patch('game.input', create=True)
    def test_12_PlayerQuits(self, mocked_input):
        '''Test player input when quiting.'''
        mocked_input.side_effect = ['q', 'y']

        p1 = pl.Player(name="Pino", playerType=0)
        p2 = pl.Player(name="danny", playerType=0)
        self.game.players = [p1, p2]

        self.game.playerAction(self.game.players[0])
        result = self.game.players[0].score
        expected = -1

        self.assertEqual(result, expected)

    @mock.patch('game.input', create=True)
    def test_13_GameRound1(self, mocked_input):
        '''Test game round when player cheats.'''
        mocked_input.side_effect = ['n', 'end']

        p1 = pl.Player(name="Pino", playerType=0)
        p2 = pl.Player(name="danny", playerType=0)
        self.game.players = [p1, p2]

        self.game.runGame()

        # check player 1 score
        result = self.game.players[0].score
        expected = 0
        self.assertEqual(result, expected)

        # check player 2 score
        result = self.game.players[1].score
        expected = 50
        self.assertEqual(result, expected)

    @mock.patch('game.input', create=True)
    def test_14_GameRound2(self, mocked_input):
        '''Test game round when player quits.'''
        mocked_input.side_effect = ['n', 'q', 'y']

        p1 = pl.Player(name="Pino", playerType=0)
        p2 = pl.Player(name="danny", playerType=0)
        self.game.players = [p1, p2]

        self.game.runGame()

        # check player 1 score
        result = self.game.players[0].score
        expected = 0
        self.assertEqual(result, expected)

        # check player 2 score
        result = self.game.players[1].score
        expected = -1
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
