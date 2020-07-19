
class Game:
    def __init__(self, player1, player2, token1, token2):
        self.player1 = player1
        self.player2 = player2
        # player names will be established
        # their preferred token established
        self.token1 = token1
        self.token2 = token2
    # the game board which will be directly interacted with by the players
    board = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]


