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
fake_list = np.array([[0, 0, 0, 1, 0, 0, 1],
                      [1, 1, 0, 1, 1, 0, 1],
                      [0, 1, 1, 1, 1, 1, 1],
                      [0, 0, 1, 1, 1, 1, 1],
                      [1, 0, 0, 1, 0, 1, 1],
                      [0, 1, 1, 1, 1, 1, 1]])


# this is the fundamental function which will check for the connect4 in each instance
def check_connect4(array, token):
    token_array = [n == token for n in array]
    print(token_array)
    token_count = (len(array) - 3)
    print(token_count)
    for token_index in range(0, token_count):
        connect4_count = 0
        for i in range(token_index, token_index + 4):
            print(f"from {token_index} @ {i}")
            if token_array[token_index]:
                connect4_count += 1
    print(token_index)
    print(token_count)
    if connect4_count == 4:
        return True
    elif token_index == (token_count - 1):
        return False


# Function to check for 4 same tokens in a horizontal row #
def check_horizontal(board, token, token_place):
    checked_row = board[token_place[0]]
    print(checked_row)
    return check_connect4(checked_row, token)


# function(s) to convert vertical elements into a list and check for 4 same tokens in a row #

# this function will convert all elements in the same position index in their respective lists (of a 2d array)
# and store it inside a list
def convert_vertical_array(board, token_place):
    position_index = token_place[1]
    vertical_array = []
    for i in range(0, 6):
        vertical_array.append(board[i][position_index])
    return vertical_array


def check_vertical(board, token, token_place):
    vertical_array = convert_vertical_array(board, token_place)
    # once array is made, the process is very similar to 'check_horizontal' function. Check there for more info.
    return check_connect4(vertical_array, token)


# Below is function to check for 4 same tokens in a vertical fashion #

# (0, 4), if reversed it would equal (0,2) #
# 0 --> 6, 1 ---> 5, 2 ----> 4, 3 ----> 3 #

# so gotta make 3 mini functions:

# the first will convert the single diagonal (left to right) into a list
# it will also check if the list has > 3 elements. If not then this list is not used (can't have connect4
# with a straight which only has 3 spaces

# The second will use the .reverse function to reverse all element places in the board array, allowing for the
# first mini-function to be used again.

# the third will convert the index of element (token_position) to it's reverse counterpart
#                     e.g.(list , (-3,2)


def convert_diagonal_array(board, token_place):
    diagonal_array = []
    row = token_place[0]
    index = token_place[1]
    finding_start = True
    while finding_start:
        if row == -1 or index == 0:
            finding_start = False
        elif index == -1 and row == 0:
            finding_start = False
        else:
            row += 1
            index += -1
    diagonal_array.append(board[row][index])
    finding_end = True

    while finding_end:
        if row == -6 or index == 6:
            if len(diagonal_array) > 3:
                return diagonal_array
                # more efficient to remove diagonals with less than 4 elements (as connect4 is not possible)
            else:
                return False
        else:
            row += -1
            index += 1
            diagonal_array.append(board[row][index])

    # this is the position in the list where we will add elements to the 'diagonal array'


# (0, 4), if reversed it would equal (0,2) #
# 0 --> 6, 1 ---> 5, 2 ----> 4, 3 ----> 3 #

def reverse_token_place(token_place):
    token_index = [6, 5, 4, 3, 2, 1, 0]
    new_token_place = (token_place[0], token_index.index(token_place[1]))
    return new_token_place


def check_diagonal(board, token, token_place):
    diagonal_array = convert_diagonal_array(board, token_place)

    if check_connect4(diagonal_array, token):
        print("heheh")
        return True
    print("not here")

    reversed_token_place = reverse_token_place(token_place)
    diagonal_array = convert_diagonal_array(board, reversed_token_place)
    if check_connect4(diagonal_array, token):
        print("here")
        return True
    else:
        return False

print(check_diagonal(fake_list, 1, (-5, 4)))