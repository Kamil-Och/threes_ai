import numpy as np
import random 
import enum

class move(enum.Enum):
    up = 0
    right = 1
    down = 2
    left = 3
    
class Board:
    def __init__(self, x = 4, y = 4, seed = None):
        self.board = np.zeros((x,y), dtype = np.int16)
        self.score = 0
        
        self.init_board(seed = seed)
        
    def init_board(self, number_of_tiles = 9, seed = None):
        if seed is None:
            seed = np.random.SeedSequence().entropy
            
        self.seed = seed
        rng = np.random.default_rng(seed)
        
        #print(self.seed)
        initial_tiles = rng.choice(self.board.size, number_of_tiles, replace = False)        
        
        for i, _ in enumerate(self.board.flat):
            if i in initial_tiles:
                self.board.flat[i] = rng.choice([1, 2, 3])
    
    def move(self, direction: move):
        # 0: up, 1: right, 2: down, 3: left
        if direction == move.up:
            new_board = np.zeros(self.board.shape, dtype = np.int16)
            
            #first column
            # 3 => 3
            # 0 => 0
            # 0 => 1
            # 1 => -1
            
            # check(3, 0) => False
            # check(0, 0) => True
            # check(0, 1) => True
            # populate -1 
            
            
            
            for x in range(self.board.shape[0]):
                for y in range(self.board.shape[1]-1):
                    a = self.board[y, x]
                    b = self.board[y+1, x]
                    
                    if self.check_if_can_move(a, b):
                        if a == 0:
                            new_board[y, x] = b
                            for i in range(y+1, self.board.shape[1]-1):
                                new_board[i, x] = self.board[i-1, x]
                        else:
                            new_board[y, x] = a + b
                            for i in range(y+1, self.board.shape[1]-1):
                                new_board[i, x] = self.board[i-1, x]
                        break
                    else:
                        new_board[y, x] = a
            self.board = new_board
        
        elif direction == move.right:
            pass
        elif direction == move.left:
            pass
        elif direction == move.down:
            pass
        
    def check_row(self, row: list):
        for i in range(len(row)-1):
            if self.check_if_can_move(row[i], row[i+1]):
                return True
        return False
    

    def check_if_can_move(self, first_value, second_value):
        if first_value == 0:
            return True
        elif first_value == 1 and second_value == 2:
            return True
        elif first_value == 2 and second_value == 1:
            return True
        elif first_value != 1 and first_value != 2 and first_value == second_value:
            return True
        else:
            return False
    
    def merge(self, first_value, second_value):
        return first_value + second_value
    
        
threes_obj = Board(seed=291287734567828204531957046342580506050)
print(threes_obj.board)
threes_obj.move(move.up)
print("after move up\n", threes_obj.board)
# threes.move(move.down)
# print(threes.board)
# threes.move(move.left)
# print(threes.board)
# threes.move(move.right)