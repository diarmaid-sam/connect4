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
                      [1, 1, 0, 1, 0, 1, 1],
                      [0, 1, 1, 1, 1, 0, 0]])


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

check_vertical(fake_list, 1, (0,2))


