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
            print(colored(f"\033[1m\n\n{game.player1}'s TURN \033[0m\n\n", game.color1))
            # select and place returns a list of two values.
            # the first being the new board, the second being the token_place
            token_place = game.select_and_place(game.token1)[1]
            if checkwinner(game.board, game.token1, token_place):
                winner = True
                player1_score += 1
                print(colored(f"{game.player1} has won the game !\n\n"
                              f"{game.player1} is on {player1_score} points", game.color1))
        else:
            print(colored(f"\033[1m\n\n{game.player2}'s TURN \033[0m\n\n", game.color2))
            token_place = game.select_and_place(game.token2)[1]
            if checkwinner(game.board, game.token2, token_place):
                winner = True
                player2_score += 1
                print(colored(f"{game.player2} has won the game !\n\n"
                              f"{game.player2} is on {player2_score} points", game.color2))

    Qcontinue = input("Would you like to play another game (y/n) ?\n\nEnter here :  ")
    Qcontinue = Qcontinue.lower()
    possible_answers = ["yes", "ye", "y", "no", "n", "nein"]
    if Qcontinue in possible_answers:
        if Qcontinue in possible_answers[0:3]:
            print(colored("\n\n[The game will restart]\n\n", "red"))
        else:
            play_again = False
            print(colored("\n\n[The game will terminate]"))






