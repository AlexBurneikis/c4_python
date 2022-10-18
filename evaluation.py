def evaluate(board):
    if board.is_game_over():
        if len(board.legal_moves()) == 0:
            return 0
        else:
            return float('-inf') if board.turn else float('inf')

    score = 0
    #find rows with 3 in a row
    for i in range(6):
        for j in range(4):
            if board.yellow[i][j] == 1 and board.yellow[i][j+1] == 1 and board.yellow[i][j+2] == 1:
                score += 9
            if board.red[i][j] == 1 and board.red[i][j+1] == 1 and board.red[i][j+2] == 1:
                score -= 9

    #find columns with 3 in a row
    for i in range(3):
        for j in range(7):
            if board.yellow[i][j] == 1 and board.yellow[i+1][j] == 1 and board.yellow[i+2][j] == 1:
                score += 9
            if board.red[i][j] == 1 and board.red[i+1][j] == 1 and board.red[i+2][j] == 1:
                score -= 9

    #find diagonals with 3 in a row
    for i in range(3):
        for j in range(4):
            if board.yellow[i][j] == 1 and board.yellow[i+1][j+1] == 1 and board.yellow[i+2][j+2] == 1:
                score += 9
            if board.red[i][j] == 1 and board.red[i+1][j+1] == 1 and board.red[i+2][j+2] == 1:
                score -= 9

    for i in range(3):
        for j in range(3, 7):
            if board.yellow[i][j] == 1 and board.yellow[i+1][j-1] == 1 and board.yellow[i+2][j-2] == 1:
                score += 9
            if board.red[i][j] == 1 and board.red[i+1][j-1] == 1 and board.red[i+2][j-2] == 1:
                score -= 9

    #find rows with 2 in a row
    for i in range(6):
        for j in range(5):
            if board.yellow[i][j] == 1 and board.yellow[i][j+1] == 1:
                score += 4
            if board.red[i][j] == 1 and board.red[i][j+1] == 1:
                score -= 4

    #find columns with 2 in a row
    for i in range(4):
        for j in range(7):
            if board.yellow[i][j] == 1 and board.yellow[i+1][j] == 1:
                score += 4
            if board.red[i][j] == 1 and board.red[i+1][j] == 1:
                score -= 4

    #find diagonals with 2 in a row
    for i in range(4):
        for j in range(5):
            if board.yellow[i][j] == 1 and board.yellow[i+1][j+1] == 1:
                score += 4
            if board.red[i][j] == 1 and board.red[i+1][j+1] == 1:
                score -= 4

    for i in range(4):
        for j in range(2, 7):
            if board.yellow[i][j] == 1 and board.yellow[i+1][j-1] == 1:
                score += 4
            if board.red[i][j] == 1 and board.red[i+1][j-1] == 1:
                score -= 4

    return score