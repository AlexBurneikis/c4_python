from evaluation import evaluate

def minimax(board, depth, alpha, beta):
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
        return best_score
