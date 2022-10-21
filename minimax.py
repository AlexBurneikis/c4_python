from evaluation import evaluate
from hashlist import hashlist

transposition_table = {}

def minimax(board, depth, alpha, beta):
    # check if the board is in the transposition table
    hash = zobrist_hash(board)
    if hash in transposition_table:
        # only return the score if the depth is equal (it will never be greater)
        if transposition_table[hash][1] == depth:
            return transposition_table[hash][0]

    if depth == 0 or board.is_game_over():
        return evaluate(board)
    if board.turn:
        best_score = float('-inf')
        for move in board.legal_moves():
            board.push(move)
            score = minimax(board, depth - 1, alpha, beta)
            board.pop()
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break

        # add to transposition table
        transposition_table[hash] = (best_score, depth)

        return best_score
    else:
        best_score = float('inf')
        for move in board.legal_moves():
            board.push(move)
            score = minimax(board, depth - 1, alpha, beta)
            board.pop()
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break

        # add to transposition table
        transposition_table[hash] = (best_score, depth)

        return best_score

def zobrist_hash(board):
    # iterate over every column and row in the board and XOR the hash of the piece in that position
    hash = 2
    for i in range(6):
        for j in range(7):
            if board.yellow[i][j] == 1:
                hash ^= hashlist[i*7 + j]
            if board.red[i][j] == 1:
                hash ^= hashlist[i*7 + j + 42]
    return hash
