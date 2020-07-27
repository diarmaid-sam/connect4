import gameclass
from get_Game_attributes import get_Game_attributes
from checkwinner import checkwinner
from termcolor import colored

player1_score = 0
player2_score = 0
play_again = True
game = get_Game_attributes()
while play_again:
    winner = False
    while not winner:
        if game.check_turn() == game.player1:
            # select and place returns a list of two values.
            # the first being the new board, the second being the token_place
            token_place = game.select_and_place(game.token1)[1]
            print(game.board)
            if checkwinner(game.board, game.token1, token_place):
                winner = True
                player1_score += 1
                print(colored(f"{game.player1} has won the game !\n\n"
                              f"{game.player1} is on {player1_score} points", game.color1))

                play_again = False



