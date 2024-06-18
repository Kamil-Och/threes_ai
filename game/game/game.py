import sys
sys.path.append("..")
import board.board as Board

class Game:
    def __init__(self):
        self.board = Board()
        self.score = 0
        self.state = 0 # Enum?
        self.next_tile = 0 
        
    def start(self):
        self.board.init_board()
    
    def move(self, direction):
        #check if the move is valid
        #update the board
        pass
    
    def get_score(self):
        #count the board histogram and calculate the score
        pass
    #TODO: game end condition: no more move or 12,288 reached
    #TODO: odds chart for the new tile initial (50 % 1 and 50 % 2)
    #      chart is dynamic based on the current board state
    #      1. 1 and 2 are the most common
    #      2. 3 is less common
    #      3. 6 is rare and so on
    #      4. should generate when i
