class Chessboard:
    board = []
    @classmethod
    def init(cls):
        for i in range(0,8):
            row = []
            for k in range(0,8):
                row.append(Square(i,k))
            board.append(row)
    def __getitem__(self, x, y):
        return board[x, y]

class Square:
    def __init__(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.piece = piece

    def hold(self, piece):
        self.piece = piece

class Path:
    def __init__(self):
        self.squares = []
    def add(self, squares):
        if isinstance(squares, list):
            self.squares.extend(squares)
        elif isinstance(squares, Square):
            self.squares.append(squares)
        else:
            raise TypeError(f"{type(squares)} is not valid type in Path")

    def __contains__(self, square):
        for sq in self.squares:
            if square.x == sq.x and square.y == sq.y:
                return True
        return False
