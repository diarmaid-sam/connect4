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
    board = np.array([[0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0],
                      [0, 1, 1, 1, 1, 1, 0],
                      [1, 1, 1, 1, 1, 1, 1]])

    def showboard(self):
        for i in Game.board:
            # prints the list in a more graphically appealing way
            print(" | ".join(str(n) for n in i))

    def select_place(self):
        invalid = True
        # Invalid = True prevents the player from exiting the while loop untill they have placed a valid integer
        # while loop takes a valid placement for token. If invalid (i.e. placement in a full column) then it asks
        # to select another
        token_place = "initialised"
        while invalid:
            Game.showboard(self)
            print(colored("\033[1m1   2   3   4   5   6   7\033[0m", "yellow"))
            try:
                placement = (int(input("\nPlease input the number of the column you would like to place your "
                                       "token : ")) - 1)
                if Game.board[0][placement] != 0:
                    print(
                        colored(f"\n------- The column you have selected (column {(placement + 1)}) is fully occupied "
                                f"-------\n\n  -------- Please select another column to place your token "
                                f"--------\n",
                                "red"))
                    continue
                    # this 'continue' immediately sends the player back to the start of the loop to re-input 'placement'
            except ValueError:
                print(colored(f"\n------- You have imputed no value |or| you have imputed a string value "
                              f"-------\n\n  -------- Please input an integer value in range 1-7 --------\n",
                              "red"))
            except IndexError:
                print(colored(f"\n------- You have imputed a value out of range 1-7 -------"
                          f"-------\n\n  -------- Please input an integer value in range 1-7 --------\n",
                          "red"))

            else:
                row_number = -1
                print(placement)
                for row in Game.board:
                    if Game.board[row_number, placement] == 0:
                        token_place = (row_number, placement)
                        print("zero")
                        break

                    else:
                        row_number += -1
                        print("reached")
                return print(token_place)


game1 = Game("diarmaid", "bob", "d", "b")
game1.select_place()
