from game import Board
from ai_move import get_move
from timeit import timeit

def main():
    board = Board()

    while not board.is_game_over():
        print(board)
        print("Turn:", "Yellow" if board.turn else "Red")
        move = get_move(board, 9)
        board.push(move)
        print("Move:", move)

    print(board)
    print(board.moves)
    print(board.result())

if __name__ == "__main__":
    #time it
    print(timeit(main, number=1))