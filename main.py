from game import Board
from ai_move import get_move

board = Board()

while not board.is_game_over():
    print(board)
    print("Legal moves:", board.legal_moves())
    print("Turn:", "Yellow" if board.turn else "Red")
    move = get_move(board)
    board.push(move)

print(board)
print("Game over")
print(board.moves)