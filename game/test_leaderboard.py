import unittest
import leaderboard as lb


class TestLeaderboardClass(unittest.TestCase):
    '''
    Unittesting of leaderboard class.
    '''

    def setUp(self):
        ''' Make leaderboard object.'''
        self.leadboard = lb.Leaderboard()

    def test_01_DefaultObject(self):
        '''Instantiate an object and check its properties.'''
        self.assertIsInstance(self.leadboard, lb.Leaderboard)

    def test_02_UpdateEmptyLeaderboard(self):
        '''Test update of an empty leaderboard.'''
        self.leadboard.updateLeaderboard(0, "test")
        result = self.leadboard.board
        expected = [(0, "test")]
        self.assertListEqual(result, expected)

    def test_03_UpdateNonEmptyLeaderboard(self):
        '''Test update of an leaderboard with information.'''
        self.leadboard.updateLeaderboard(3, "test1")
        self.leadboard.updateLeaderboard(1, "test2")
        self.leadboard.updateLeaderboard(7, "test3")
        result = self.leadboard.board
        expected = [(7, "test3"), (3, "test1"), (1, "test2")]
        self.assertListEqual(result, expected)
