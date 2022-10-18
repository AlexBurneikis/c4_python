class Board:
    def __init__(self):
        self.yellow = [[0 for i in range(7)] for j in range(6)]
        self.red = [[0 for i in range(7)] for j in range(6)]
        #yellow is True, red is False
        self.turn = True
        
        self.last_move = None
        
    def __str__(self):
        #combine the two boards into one using X for yellow and O for red
        board = [[0 for i in range(7)] for j in range(6)]
        for i in range(6):
            for j in range(7):
                if self.yellow[i][j] == 1:
                    board[i][j] = "X"
                elif self.red[i][j] == 1:
                    board[i][j] = "O"
        #print the board
        for i in range(6):
            print(board[i])
        return ""

    def push(self, column):
        #if the column is full, throw an error
        if self.yellow[0][column] == 1 or self.red[0][column] == 1:
            raise Exception("Column is full")

        #find the lowest empty space in the column
        for i in range(5, -1, -1):
            if self.yellow[i][column] == 0 and self.red[i][column] == 0:
                if self.turn:
                    self.yellow[i][column] = 1
                else:
                    self.red[i][column] = 1
                break
        
        #change the turn
        self.turn = not self.turn
        
        self.last_move = column

    def pop(self):
        column = self.last_move
        for i in range (0, 6, 1):
            if self.yellow[i][column] or self.red[i][column]:
                self.yellow[i][column] = 0
                self.red[i][column] = 0
                break
                
        self.turn = not self.turn
                

        
    def legal_moves(self):
        #return the numbers of the columns that are not full
        return [i for i in range(7) if self.yellow[0][i] == 0 and self.red[0][i] == 0]

    def is_game_over(self):
        #check for four in a row
        for i in range(6):
            for j in range(4):
                if self.yellow[i][j] == 1 and self.yellow[i][j+1] == 1 and self.yellow[i][j+2] == 1 and self.yellow[i][j+3] == 1:
                    return True
                if self.red[i][j] == 1 and self.red[i][j+1] == 1 and self.red[i][j+2] == 1 and self.red[i][j+3] == 1:
                    return True
                    
        #check for four in a column
        for i in range(3):
            for j in range(7):
                if self.yellow[i][j] == 1 and self.yellow[i+1][j] == 1 and self.yellow[i+2][j] == 1 and self.yellow[i+3][j] == 1:
                    return True
                if self.red[i][j] == 1 and self.red[i+1][j] == 1 and self.red[i+2][j] == 1 and self.red[i+3][j] == 1:
                    return True
                    
        #check for four in a diagonal
        for i in range(3):
            for j in range(4):
                if self.yellow[i][j] == 1 and self.yellow[i+1][j+1] == 1 and self.yellow[i+2][j+2] == 1 and self.yellow[i+3][j+3] == 1:
                    return True
                if self.red[i][j] == 1 and self.red[i+1][j+1] == 1 and self.red[i+2][j+2] == 1 and self.red[i+3][j+3] == 1:
                    return True
        
        for i in range(3):
            for j in range(3, 7):
                if self.yellow[i][j] == 1 and self.yellow[i+1][j-1] == 1 and self.yellow[i+2][j-2] == 1 and self.yellow[i+3][j-3] == 1:
                    return True
                if self.red[i][j] == 1 and self.red[i+1][j-1] == 1 and self.red[i+2][j-2] == 1 and self.red[i+3][j-3] == 1:
                    return True

        #check for a tie
        if len(self.legal_moves()) == 0:
            return True

        return False
