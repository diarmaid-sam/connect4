from gameclass import Game
from termcolor import colored


def get_Game_attributes():
    # def __init__(self, player1, player2, token1, token2, color1, color2):
    # Takes a suitable name
    print(colored("The following will ask for your name, please enter a suitable name which has at least 1 character",
                  "red"))
    incorrect_player_name = True
    while incorrect_player_name:
        player1 = input("Will player1 please enter your name : ")
        if not len(player1) > 0:
            print(colored(f"\nPlayer1 you have not entered a name. Please try again", "red"))
        else:
            player2 = input("Player2 can you please enter your name : ")
            if not len(player2) > 0:
                print(colored(f"\nPlayer2 you have not entered a name. Please try again", "red"))
            else:
                incorrect_player_name = False

    # prints available colors to choose from
    print("\n\033[1mAVAILABLE COLOURS \033[0m")
    available_colors = ["grey", "white", "red", "green", "yellow", "blue", "magenta", "cyan"]
    for i in available_colors:
        print(" ".join(str(n) for n in i))

    incorrect_colour1 = True
    incorrect_colour2 = True
    while incorrect_colour1:
        try:
            color1 = input(f"\n{player1} please enter your desired colour from the list above : ")
            available_colors.remove(color1.lower())
            incorrect_colour1 = False
            print("\n\033[1mAVAILABLE COLOURS \033[0m")
        except ValueError:
            print(colored("\n--- Please input the a valid colour name from the list above ---", "red"))
    while incorrect_colour2:
        try:
            print("\n\033[1mAVAILABLE COLOURS \033[0m")
            for i in available_colors:
                print(" ".join(str(n) for n in i))
            color2 = input(f"\n{player2} please enter your desired colour from the list above : ")
            available_colors.remove(color2.lower())
            incorrect_colour2 = False
        except ValueError:
            print(colored("\n--- Please input the a valid colour name from the list above ---", "red"))

    print(colored("\nFor the following please input one character you wish to use to represent your token\n"
                  "---- The first letter you place will represent your token ----", "red"))
    incorrect_token_len = True
    while incorrect_token_len:
        try:
            token1 = str(input(f"\n'{player1}' please enter the token you wish to play with : "))[0]
            incorrect_token_len = False
        except IndexError:
            print(colored(f"\n{player1} you have not entered a token. Please try again", "red"))
    incorrect_token_len = True
    while incorrect_token_len:
        try:
            token2 = str(input(f"\n'{player2}' please enter the token you wish to play with : "))[0]
            incorrect_token_len = False
        except IndexError:
            print(colored(f"\n{player2} you have not entered a token. Please try again", "red"))

    return Game(player1, player2, token1, token2, color1, color2)
