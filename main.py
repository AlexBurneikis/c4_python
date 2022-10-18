from game import Board

board = Board()

while not board.is_game_over():
    print(board)
    print("Legal moves:", board.legal_moves())
    print("Turn:", "Yellow" if board.turn else "Red")
    move = int(input("Enter a move: "))
    board.push(move)

print(board)