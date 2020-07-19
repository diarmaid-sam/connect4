import numpy as np

class Game:
    def __init__(self, player1, player2, token1, token2):
        # player names will be established when passed as parameter
        self.player1 = player1
        self.player2 = player2
        # initialise this attribute of who's turn as player1
        self.whoturn = player1
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
            return (" | ".join(str(n) for n in i))

    def available_place(self):
        for row in Game.board:
            places = []
            places = places.extend(np.argwhere(row = 0))






    def playerturn(self):
        Game.showboard(self)
        placement = int(input("1   2   3   4   5   6   7\nPlease input the number you would like to place your token : "))
        # now we need to place the token at the correct index of this list
        # if self.whoturn == Game.player1:





game1 = Game("diarmaid","bob","d","b")
game1.playerturn()
game1.available_places()
