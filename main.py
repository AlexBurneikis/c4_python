from game import Board
from ai_move import get_move
from timeit import timeit

def main():
    board = Board()

    while not board.is_game_over():
        print(board)
        print("Turn:", "Yellow" if board.turn else "Red")
        move = get_move(board, 12)
        board.push(move)
        print("Move:", move)

    print(board)
    print(board.moves)
    print(board.result())

if __name__ == "__main__":
    print(timeit(main, number=1))