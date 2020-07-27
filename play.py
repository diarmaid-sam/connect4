from gameclass import Game
from get_Game_attributes import get_Game_attributes
from checkwinner import checkwinner
from termcolor import colored
import numpy as np
import random

player1_score = 0
player2_score = 0
play_again = True
attributes = get_Game_attributes()
while play_again:
    game_code = Game(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5])
    winner = False
    while not winner:
        if game_code.check_turn() == game_code.player1:
            print(colored(f"\033[1m\n\n{game_code.player1}'s TURN \033[0m\n\n", game_code.color1))
            # 'select_and_place' returns a list of two values.
            # the first being the new board, the second being the token_place
            token_place = game_code.select_and_place(game_code.token1)[1]
            if checkwinner(game_code.board, game_code.token1, token_place):
                winner = True
                player1_score += 1
                print(colored(f"{game_code.player1} has won the game !\n\n"
                              f"{game_code.player1} is on {player1_score} point(s)", game_code.color1))
        else:
            print(colored(f"\033[1m\n\n{game_code.player2}'s TURN \033[0m\n\n", game_code.color2))
            token_place = game_code.select_and_place(game_code.token2)[1]
            if checkwinner(game_code.board, game_code.token2, token_place):
                winner = True
                player2_score += 1
                print(colored(f"{game_code.player2} has won the game !\n\n"
                              f"{game_code.player2} is on {player2_score} point(s)", game_code.color2))

    Q_continue = input("Would you like to play another game (y/n) ?\n\nEnter here :  ")
    Q_continue = Q_continue.lower()
    possible_answers = ["yes", "ye", "y", "no", "n", "nein"]
    if Q_continue in possible_answers:
        if Q_continue in possible_answers[0:3]:
            print(colored("\n\n[The game will restart]\n\n", "red"))
        else:
            play_again = False
            print(colored("\n\n[The game will terminate]"))






