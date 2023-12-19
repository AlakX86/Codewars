def is_solved(board):
    def check_winner():
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != 0 or board[0][i] == board[1][i] == board[2][i] != 0:
                return board[i][i]

        if board[0][0] == board[1][1] == board[2][2] != 0 or board[0][2] == board[1][1] == board[2][0] != 0:
            return board[1][1]

        return 0

    winner = check_winner()

    if winner != 0:
        return winner
    elif any(0 in row for row in board):
        return -1 
    else:
        return 0