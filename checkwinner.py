import numpy as np

# here is the final and single function 'checkwinner' which will check for all combinations for connect4 with
# a given token placement of the player.


def checkwinner(board, token, token_place):
    if check_horizontal(board, token, token_place):
        return True
    elif check_vertical(board, token, token_place):
        return True
    elif check_diagonal(board, token, token_place):
        return True
    else:
        return False


# ---------------------- Below are the functions for function 'checkwinner' ------------------------ #

# this is the fundamental function which will check for the connect4 in each instance (once an array is compiled)
def check_connect4(array, token):
    token_count = (len(array) - 3)
    token_array = [n == token for n in array]
    for token_index in range(0, token_count):
        connect4_count = 0
        for i in range(token_index, token_index + 4):
            if token_array[i]:
                connect4_count += 1
                if connect4_count == 4:
                    return True
            else:
                connect4_count = 0
    return False


# Function to check for 4 same tokens in a horizontal row #
def check_horizontal(board, token, token_place):
    checked_row = board[token_place[0]]
    return check_connect4(checked_row, token)


# function(s) to convert vertical elements into a list and check for 4 same tokens in a row #

# this function will convert all elements in the same column index in their respective lists (of a 2d array)
# and store it inside a list
def convert_vertical_array(board, token_place):
    position_index = token_place[1]
    vertical_array = []
    for i in range(0, 6):
        vertical_array.append(board[i][position_index])
    return vertical_array


def check_vertical(board, token, token_place):
    vertical_array = convert_vertical_array(board, token_place)
    # once array is made, the process is the same for diagonals, verticals and horizontals
    return check_connect4(vertical_array, token)


# Below is function to check for 4 same tokens in a vertical fashion #

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


def reverse_token_place(token_place):
    token_index = [6, 5, 4, 3, 2, 1, 0]
    new_token_place = (token_place[0], token_index.index(token_place[1]))
    return new_token_place


def check_diagonal(board, token, token_place):
    diagonal_array = convert_diagonal_array(board, token_place)
    # i.e. if diagonal array has less than 4 values
    if not diagonal_array:
        pass
    else:
        if check_connect4(diagonal_array, token):
            return True
    reversed_token_place = reverse_token_place(token_place)
    # takes the mirror image position of the token position so that the 'convert_diagonal_array' can be reused
    reversed_array = np.fliplr(board)
    # this reverses the order of the array
    diagonal_array = convert_diagonal_array(reversed_array, reversed_token_place)
    if not diagonal_array:
        return False
    else:
        if check_connect4(diagonal_array, token):
            return True
        else:
            return False
