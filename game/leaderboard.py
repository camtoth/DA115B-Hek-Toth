import pickle


class Leaderboard:
    '''
    Class that makes the leaderboard.
    '''

    def __init__(self):
        '''
        Constructor of leaderboard class.
        Attributes:
        board (list): List containg all scores (standard empty).
        '''
        self.board = []

    def updateLeaderboard(self, score, name):
        '''
        Method adds a new score and order it starting with the highest score.
        Parameters:
        score (int): new score to add.
        name (string): player name of new score.
        '''
        # appends new score and name to the end of the leaderboard
        self.board.append((score, name))
        # sorts the leaderboard based on the score in reverse order
        self.board.sort(key=lambda x: x[0], reverse=True)

    def printLeaderboard(self):
        '''
        Method that prints the leaderboard.
        '''
        print(" --- HIGHEST SCORES ---")
        for i in range(len(self.board)):
            print(self.board[i])

    def saveLeaderboard(self):
        '''
        Method that saves the current leaderboard.
        Data is stored in a pickle file.
        '''
        with open('leadearboard_data.pkl', 'wb') as pickle_out:
            pickle.dump(self.board, pickle_out, pickle.HIGHEST_PROTOCOL)

    def loadLeaderboard(self):
        '''
        Method read leaderboard file.
        '''
        try:
            with open('leadearboard_data.pkl', 'rb') as pickle_in:
                self.board = pickle.load(pickle_in)
        except BaseException:
            pass
