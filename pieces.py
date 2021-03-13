from abc import ABC

from .board import *

class Pieces(ABC):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def valid_path(self):
        pass
    

class Pawn(Pieces):
    def valid_path(self):
        
        if self.y == 1 or self.y == 7:
            max_square = 2
        else:
            max_square = 1
        
        if self.side == 'white':

        else:


class Bishop(Pieces):
    pass

class Rock(Pieces):
    pass

class Knight(Pieces):
    pass

class Queen(Pieces):
    pass

class King(Pieces):
    pass

if __name__ == '__main__':
    print('OK')


