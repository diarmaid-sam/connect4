import numpy as np
from termcolor import colored


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
    # the game board which will be directly interacted with by the
    board = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0],
                    [0, 1, 1, 1, 1, 1, 0],
                    [1, 1, 1, 1, 1, 1, 1]])

    def showboard(self):
        for i in Game.board:
            # prints the list in a more graphically appealing way
            print(" | ".join(str(n) for n in i))

    def select_placee(self):
        Game.showboard(self)
        print(colored("\033[1m1   2   3   4   5   6   7\033[0m", "yellow"))
        invalid = True
        # while loop takes a valid placement for token. If invalid (i.e. placement in a full column) then it asks
        # to select another
        while invalid:
            placement = (int(input("\nPlease input the number you would like to place your token : "))-1)
            if Game.board[0][placement] != 0:
                print(colored(f"\n------- The column you have selected (column {(placement + 1)}) is fully occupied "
                              f"-------\n\n  -------- Please select another column to place your token --------\n",
                              "red"))
            else:
                for row in Game.board:
                    row_number = -1
                    if Game.board[row_number, placement] == 0:
                        token_place = Game.board[row_number, placement]
                        print("non-zero")
                        break
                    else:
                        row_number += -1
                        print("reached")
                return token_place







    def select_place(self):
        token_place = False
        # token_place is the variable which records the exact index in which the player's token will be placed
        # this variable is required to ensure that a suitable token place is found (if a column is full then
        # the user will have to find another place for it

        while not token_place:
            Game.showboard(self)
            print(colored("\033[1m1   2   3   4   5   6   7\033[0m", "yellow"))
            Error = True
            while Error:
                try:
                    # (for placement) this allows for the placement number to be directly used to describe the index of the
                    # token placement
                    placement = (int(input("\nPlease input the number you would like to place your token : "))-1)
                    # token_place is the variable which records the exact index in which the player's token will be placed
                    # '-1' value will start from the last value in the list
                except ValueError:

                row_number = -1
                for x in range (0,6):
                    if Game.board[row_number, placement] == 0:
                        token_place = Game.board[row_number, placement]
                        print("non-zero")
                        break
                        #before you left, you are going to rearrange the file to check the first element of the selected
                        #column of the game board. if it doesn't = 0 (i.e. isnt empty) you will ask them to choose another
                    else:
                        row_number += -1
                        print("reached")
                if:
                    print(colored(f"\n------- The column you have selected (column {(placement+1)}) is fully occupied "
                                  f"-------\n\n  -------- Please select another column to place your token --------\n",
                                  "red"))
                else:
                    ("Placement found")










game1 = Game("diarmaid","bob","d","b")

game1.select_place()