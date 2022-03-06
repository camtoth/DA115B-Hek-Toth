import pickle

class Leaderboard:
    
    def __init__(self):
        self.board = []
        
    def updateLeaderboard(self, score, name):
        # appends new score and name to the end of the leaderboard
        self.board.append((score, name))
        #sorts the leaderboard based on the score in reverse order
        self.board.sort(key = lambda x: x[0], reverse = True)
        
    def printLeaderboard(self):
        print(" --- HIGHEST SCORES ---")
        for i in range(len(self.board)):
            print(self.board[i])
            
    def saveLeaderboard(self):
        with open('leadearboard_data.pkl', 'wb') as pickle_out:
            pickle.dump(self.board, pickle_out, pickle.HIGHEST_PROTOCOL)

    def loadLeaderboard(self):
        try:
            with open('leadearboard_data.pkl', 'rb') as pickle_in:
                self.board = pickle.load(pickle_in)
        except BaseException:
            pass