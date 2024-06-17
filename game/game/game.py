import sys
sys.path.append("..")
import board.board as Board

class Game:
    def __init__(self):
        self.board = Board()
        self.score = 0
        self.state = 0 # Enum?
        self.next_tiles = []
        
    def start(self):
        self.board.init_board()
    
    def move(self, direction):
        pass
    
    def get_score(self):
        pass
    