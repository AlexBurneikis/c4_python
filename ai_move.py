from minimax import minimax
from evaluation import evaluate
import multiprocessing as mp

def process_function(board, move, depth, queue):
    board.push(move)
    score = minimax(board, depth - 1, float('-inf'), float('inf'))

    queue.put((score, move))

def get_move(board, depth):
    best_score = float('-inf')
    best_move = board.legal_moves()[0]

    processes = []
    queue = mp.Queue()

    for move in board.legal_moves():
        board_copy = board.copy()
        process = mp.Process(target=process_function, args=(board_copy, move, depth, queue))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    while not queue.empty():
        score, move = queue.get()

        if not board.turn: score = -score

        if score > best_score:
            best_score = score
            best_move = move

    return best_move
