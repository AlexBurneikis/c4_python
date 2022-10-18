from minimax import minimax
from evaluation import evaluate

def get_move(board):
    best_score = float('-inf')
    best_move = board.legal_moves()[0]
    for move in board.legal_moves():
        board.push(move)
        score = minimax(board, 6, float('-inf'), float('inf'))
        board.pop()

        if not board.turn: score = -score

        if score > best_score:
            best_score = score
            best_move = move

    return best_move
