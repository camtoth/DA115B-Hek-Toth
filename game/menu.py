import game
import leaderboard as lb


class Menu:
    '''
    Class that makes the program menu.
    '''
    def __init__(self):
        '''
        Constructor of menu class.
        Attributes:
        leaderboard (leaderboard object): leaderboard of player highscores.
        new_game (game object): object of new game.
        '''
        self.leaderboard = lb.Leaderboard()
        self.new_game = game.Game(self.leaderboard)

    def menuloop(self):
        '''
        Method that runs the program menu.
        '''
        # loads leaderboard from file
        self.leaderboard.loadLeaderboard()
        while(True):
            # print main menu and take input
            print("1 - Show rules\n2 - Start new game\n" +
                  "3 - Show leaderboard\n4 - Help\n5 - Exit")

            try:
                selection = int(input("> "))
                if selection == 1:
                    self.new_game.showRules()

                elif selection == 2:
                    self.submenuloop()
                elif selection == 3:
                    self.leaderboard.printLeaderboard()
                elif selection == 4:
                    print("Type 'end' during the game  to win!")
                elif selection == 5:
                    break

            except BaseException:
                pass

    def submenuloop(self):
        '''
        Method that runs an in-game menu to make in-game changes.
        '''
        self.new_game.chooseRules()
        self.new_game.choosePlayers()
        self.new_game.output(
            "1 - Change player name\n2 - Start game\n3 - Quit")

        # 1 - Change player name
        try:
            subselection = int(input())
            while(subselection == 1):
                print("Input 1 to rename " +
                      self.new_game.players[0].name +
                      " or 2 to rename " +
                      self.new_game.players[1].name)

                try:
                    player_ID = int(input())
                    print("Enter new name: ")
                    new_name = input()
                    self.new_game.changeName(new_name, player_ID)
                    self.new_game.output(
                        "1 - Change player name\n2 - Start game\n3 - Quit")
                    subselection = int(input())
                except BaseException:
                    pass

            # 2 - Start game
            if subselection == 2:
                self.new_game.runGame()

            # 3 - Quit
            elif subselection == 3:
                exit()

        except BaseException:
            pass
