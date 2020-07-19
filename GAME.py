
class Game:
    def __init__(self, player1, player2, token1, token2):
        self.player1 = player1
        self.player2 = player2
        # player names will be established when passed as parameter
        # their preferred token established when passed as parameter
        self.token1 = token1
        self.token2 = token2
    # the game board which will be directly interacted with by the players
    board = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]
    def showboard(self):
        for i in Game.board:
            # prints the list in a more graphically appealing way
            print(" | ".join(str(n) for n in i))



    def playerturn(self, myturn):
        Game.showboard(self)
        placement = int(input("1   2   3   4   5   6   7\nPlease input the number you would like to place your token :"))



game1 = Game("diarmaid","bob","d","b")
game1.playerturn("player1")
