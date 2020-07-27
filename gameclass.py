import numpy as np
from termcolor import colored


class Game:
    def __init__(self, player1, player2, token1, token2, color1, color2):
        # player names will be established when passed as parameter
        self.player1 = player1
        self.player2 = player2
        # initialise this attribute of who's turn as player1
        # their preferred token established when passed as parameter
        self.token1 = token1
        self.token2 = token2
        self.color1 = color1
        self.color2 = color2

    # the game board which will be directly interacted with by the
    board = np.array([["0", "0", "0", "0", "0", "0", "0"],
                      ["0", "0", "0", "0", "0", "0", "0"],
                      ["0", "0", "0", "0", "0", "0", "0"],
                      ["0", "0", "0", "0", "0", "0", "0"],
                      ["0", "0", "0", "0", "0", "0", "0"],
                      ["0", "0", "0", "0", "0", "0", "0"]])

    def check_turn(self):
        # counts number of tokens to help determine who's turn it is
        # (np.count_nonzero will count instances of an element in array)
        token_count = np.count_nonzero(Game.board != "0")
        if token_count % 2 == 0:
            # '%' is modulus; returns remainder. even numbers have no remainder.
            whosturn = self.player1
        else:
            whosturn = self.player2
        return whosturn

    def what_token(self, whosturn):
        token = 0
        if whosturn == self.player1:
            token == self.token1
        else:
            token == self.token2
        return token

    def what_color(self, whosturn):
        current_color = 0
        if whosturn == self.player1:
            current_color == self.color1
        else:
            current_color == self.color2
        return current_color

    def showboard(self):
        for i in Game.board:
            # prints the list in a more graphically appealing way
            print(" | ".join(str(n) for n in i))

    def select_and_place(self, token):
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
                if Game.board[0][placement] != "0":
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

            # here we find the co-ordinates of the first available place to put a token for the selected column and
            # return the coordinates in the tuple 'token_place'
            else:
                row_number = -1
                for row in Game.board:
                    if Game.board[row_number, placement] == "0":
                        token_place = (row_number, placement)
                        break

                    else:
                        row_number += -1
            # using 'token_place' do we then place the player's token at the desired coordinates
            self.board[token_place[0], token_place[1]] = token
            return [self.board, token_place]





