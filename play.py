from gameclass import Game
from checkwinner import checkwinner
import termcolor

# def __init__(self, player1, player2, token1, token2, color1, color2):

player1 = input("Will player1 please enter your name : ")
player2 = input("Will player2 please enter your name : ")


print("\n\033[1mAVAILABLE COLOURS \033[0m")
available_colors = ["grey", "white", "red", "green", "yellow", "blue", "magenta", "cyan"]
for i in available_colors:
    print(" ".join(str(n) for n in i))
color1 = input(f"\n{player1} please enter your desired colour from the list above : ")
available_colors.remove(color1.lower())
print("\n\033[1mAVAILABLE COLOURS \033[0m")
available_colors = ["grey", "white", "red", "green", "yellow", "blue", "magenta", "cyan"]
for i in available_colors:
    print(" ".join(str(n) for n in i))
color2 = input(f"\n{player2} please enter your desired colour from the list above : ")



token1 = input(f"\n'{player1}' please enter the token you wish to play with : ")
token2 = input(f"'{player2}' please enter the token you wish to play with : ")



