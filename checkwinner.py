import numpy as np


# ([  [0, 0, 0, 0, 1, 0, 0],
#    [0, 0, 0, 0, 1, 0, 0],
#    [0, 0, 0, 0, 1, 0, 0],
#    [0, 0, 1, 0, 1, 0, 0],
#    [0, 1, 1, 1, 1, 1, 0],
#    [1, 1, 1, 1, 1, 1, 1]     ])

# these functions should check all possible combinations from the placed token. This would be more time efficient
# like much much more time efficient. just pass
def checkwinner(board, token, token_place):
    pass



# ---------------------- Below are the functions for function 'checkwinner' ------------------------ #
fake_list = np.array([[0, 0, 0, 0, 0, 1, 1],
                      [1, 1, 0, 1, 0, 1, 1],
                      [0, 1, 1, 1, 1, 0, 0],
                      [1, 0, 1, 0, 0, 1, 1],
                      [1, 1, 0, 1, 0, 0, 1],
                      [0, 1, 1, 1, 1, 0, 0]])

# Function to check for 4 same tokens in a horizontal row #
def check_horizontal(board, token, token_place):
    checked_row = board[token_place[0]]
    print(checked_row)
    # takes row of the placed token, distinguishes player's tokens from other tokens (marked with 'True')
    player_board_placements = (checked_row == token)
    print(player_board_placements)
    # e.g. [True, False, True, True, True, True, False]
    # only required to iterate over the first 4 elements to cover the whole row
    for element in range(0, 4):
        # creates the range in which the elements can be iterated over
        connect4_counter = 0
        for i in range(element, element+4):
            if player_board_placements[i] == True:
                connect4_counter += 1

        if connect4_counter == 4:
            winner = True
    if winner:
        return winner
    else:
        return False
# function(s) to convert vertical elements into a list and check for 4 same tokens in a row #

# this function will convert all elements in the same position index in their respective lists (of a 2d array)
# and store it inside a list
def convert_vertical_array(board, token_place):
    position_index = token_place[1]
    vertical_array = []
    for i in range(0,6):
        vertical_array.append(board[i][position_index])
    return vertical_array

def check_vertical(board, token, token_place):
    vertical_array = convert_vertical_array(board, token_place)
    # once array is made, the process is very similar to 'check_horizontal' function. Check there for more info.
    winner = False
    for element in range(0,3):
        connect4_counter = 0
        for i in range(element, element+4):
            if vertical_array[i] == token:
                connect4_counter +=1

        if connect4_counter == 4:
            winner = True
    if winner:
        return winner
    else:
        return False

# Below is function to check for 4 same tokens in a vertical fashion #
# fake_list = np.array([[0, 0, 0, 0, 0, 1, 1],
#                       [1, 1, 0, 1, 0, 1, 1],
#                       [0, 1, 1, 1, 1, 0, 0],
#                       [1, 0, 1, 0, 0, 1, 1],
#                       [1, 1, 0, 1, 0, 0, 1],
#                       [0, 1, 1, 1, 1, 0, 0]])

 # (0, 4), if reversed it would equal (0,2) #
 # 0 --> 6, 1 ---> 5, 2 ----> 4, 3 ----> 3 #

# so gotta make 3 mini functions:

# the first will convert the single diagonal (left to right) into a list
# it will also check if the list has > 3 elements. If not then this list is not used (can't have connect4
# with a straight which only has 3 spaces

# The second will use the .reverse function to reverse all element places in the board array, allowing for the
# first mini-function to be used again.

# the third will convert the index of element (token_position) to it's reverse counterpart

def convert_diagonal_array(board, token_place):

