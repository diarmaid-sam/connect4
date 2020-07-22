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


fake_list = np.array([[0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 1], [0, 1, 1, 1, 1, 0, 0]])


def check_horizontal(board, token, token_place):
    checked_row = board[token_place[0]]
    print(checked_row)
    connect4_counter = 0
    element_tracker = 0
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
            return winner
        else:
            winner = False



print(check_horizontal(fake_list, 1, (1, 0)))

