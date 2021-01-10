# Python3 program to find the next optimal move for a player
PLAYER, OPPONENT = 'x', 'o'
EMPTY_CELL = '_'
INF = 1000
MATRIX_SIZE = 3


def main():
    # Driver code
    board = [
        ['_', 'o', 'o'],
        ['x', 'x', 'x'],
        ['x', 'o', 'o']
    ]
    who_won = evaluate(board)
    if who_won == -10:
        print("won O")
    elif who_won == 10:
        print("won x")

    best_move = find_best_move(board)

    print("The Optimal Move is :")
    print("ROW:", best_move[0], " COL:", best_move[1])


# This function returns true if there are moves
# remaining on the board. It returns false if
# there are no moves left to play.
def is_moves_left(board):
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            if (board[i][j] == EMPTY_CELL):
                return True
    return False


# This is the evaluation function as discussed
# in the previous article ( http://goo.gl/sJgv68 )
def evaluate(b):
    # TODO do better to check termination state for infinite size of game field
    # Checking for Rows for X or O victory.
    for row in range(MATRIX_SIZE):
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
            if (b[row][0] == PLAYER):
                return 10
            elif (b[row][0] == OPPONENT):
                return -10

    # Checking for Columns for X or O victory.
    for col in range(MATRIX_SIZE):

        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):

            if (b[0][col] == PLAYER):
                return 10
            elif (b[0][col] == OPPONENT):
                return -10

    # Checking for Diagonals for X or O victory.
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):

        if (b[0][0] == PLAYER):
            return 10
        elif (b[0][0] == OPPONENT):
            return -10

    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):

        if (b[0][2] == PLAYER):
            return 10
        elif (b[0][2] == OPPONENT):
            return -10

    # Else if none of them have won then return 0
    return 0


# This is the minimax function. It considers all
# the possible ways the game can go and returns
# the value of the board
def minimax(board, depth, is_maxer):
    score = evaluate(board)

    # If Maximizer has won the game return his/her
    # evaluated score
    if score == 10:
        return score

    # If Minimizer has won the game return his/her
    # evaluated score
    if score == -10:
        return score

    # If there are no more moves and no winner then
    # it is a tie
    if is_moves_left(board) == False:
        return 0

    # If this maximizer's move
    if is_maxer:
        best = -INF

        # Traverse all cells
        for i in range(MATRIX_SIZE):
            for j in range(MATRIX_SIZE):

                # Check if cell is empty
                if (board[i][j] == EMPTY_CELL):
                    # Make the move
                    board[i][j] = PLAYER

                    # Call minimax recursively and choose
                    # the maximum value
                    best = max(best, minimax(board,
                                             depth + 1,
                                             not is_maxer))

                    # Undo the move
                    board[i][j] = EMPTY_CELL
        return best

    # If this minimizer's move
    else:
        best = INF

        # Traverse all cells
        for i in range(3):
            for j in range(3):

                # Check if cell is empty
                if board[i][j] == EMPTY_CELL:
                    # Make the move
                    board[i][j] = OPPONENT

                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(best, minimax(board, depth + 1, not is_maxer))

                    # Undo the move
                    board[i][j] = EMPTY_CELL
        return best


# This will return the best possible move for the player
def find_best_move(board):
    best_val = -INF
    best_move = (-1, -1)

    # Traverse all cells, evaluate minimax function for
    # all empty cells. And return the cell with optimal
    # value.
    for i in range(3):
        for j in range(3):

            # Check if cell is empty
            if (board[i][j] == EMPTY_CELL):

                # Make the move
                board[i][j] = PLAYER

                # compute evaluation function for this
                # move.
                move_val = minimax(board, 0, False)

                # Undo the move
                board[i][j] = EMPTY_CELL

                # If the value of the current move is
                # more than the best value, then update
                # best/
                if (move_val > best_val):
                    best_move = (i, j)
                    best_val = move_val

    print("The value of the best Move is :", best_val)
    print()
    return best_move


if __name__ == "__main__":
    main()

# This code is contributed by divyesh072019
# source https://www.guru99.com/learn-python-main-function-with-examples-understand-main.html
