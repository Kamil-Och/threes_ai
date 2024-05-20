import numpy as np
import random 
import enum

class move(enum.Enum):
    up = 0
    right = 1
    down = 2
    left = 3
    
class threes:
    def __init__(self, x = 4, y = 4, seed = None):
        self.board = np.zeros((x,y), dtype = np.int16)
        self.score = 0
        
        self.init_board(seed = seed)
        
    def init_board(self, number_of_tiles = 9, seed = None):
        if seed is None:
            seed = np.random.SeedSequence().entropy
            
        self.seed = seed
        rng = np.random.default_rng(seed)
        
        initial_tiles = rng.choice(self.board.size, number_of_tiles, replace = False)        
        
        for i, _ in enumerate(self.board.flat):
            if i in initial_tiles:
                self.board.flat[i] = rng.choice([1, 2, 3])
    
    def move(self, direction: move):
        # 0: up, 1: right, 2: down, 3: left
        if direction == move.up:
            new_board = np.zeros(self.board.shape, dtype = np.int16)
            
            for x in range(self.board.shape[0]):
                print("x", x)
                for y in range(self.board.shape[1]-1):
                    a = self.board[y, x]
                    b = self.board[y+1, x]
                    
                    if self.check_if_can_move(a, b):
                        if a == 0:
                            new_board[y, x] = b
                            print(f"new_board[{y}, {x}] = {b}")
                            for i in range(y+1, self.board.shape[1]-1):
                                print(f"new_board[{i}, {x}] = {self.board[i, x]}")
                                new_board[i, x] = self.board[i-1, x]
                        else:
                            new_board[y, x] = a + b
                            print(f"new_board[{y}, {x}] = {a+b}")
                            for i in range(y+1, self.board.shape[1]-1):
                                print(f"new_board[{i}, {x}] = {self.board[i, x]}")
                                new_board[i, x] = self.board[i-1, x]
                        break
                    else:
                        new_board[y, x] = a
                        print(f"new_board[{y}, {x}] = {a}")
            print(new_board)
                    
                    
                    
        
        elif direction == move.right:
            self.board = np.rot90(self.board, 2)
        elif direction == move.down:
            self.board = np.rot90(self.board, 3)

    def check_if_can_move(self, a, b):
        if a == 0:
            return True
        else:
            return self.check_merges(a, b)
    
    def check_merges(self, a, b):
        if a == 0 or b == 0:
            return False
        
        if a == 1 and b == 2:
            return True
        elif a == 2 and b == 1:
            return True
        elif a != 1 and a != 2 and a == b:
            return True
        else:
            return False
        
threes = threes()
print(threes.board)
threes.move(move.up)