import numpy as np

class Board:
    def __init__(self, rows = 4, columns = 4, seed = None):
        self.tiles = np.zeros((rows, columns), dtype = np.int16)
        self.seed = seed
        
    def init_board(self):
        rng = np.random.default_rng(self.seed)
        initial_tiles = rng.choice(self.tiles.size, 9, replace = False)
        
        for i, _ in enumerate(self.tiles.flat):
            if i in initial_tiles:
                self.tiles.flat[i] = rng.choice([1, 2, 3])

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
    
    def move_row(self, row):
        new_row = []
        
        for cell_number in range(len(row)-1):
            first_cell = row[cell_number]
            next_cell = row[cell_number+1]
            
            if self.check_if_can_move(first_cell, next_cell):
                new_row.append(first_cell+next_cell)
                break
            else:
                new_row.append(first_cell)
            
        if len(new_row) == len(row)-1:
            new_row.append(row[-1])
        elif len(new_row) < len(row)-1:
            for j in range(len(row)-1-len(new_row), 0, -1):
                new_row.append(row[-j])
            new_row.append(-1)
            
        return new_row
    
    def insert_new_tile(self, value):
        pass
    
    def sum_score(self, value):
        pass 
    
    
if __name__ == "__main__":
    board = Board()
    #print(board.board)
    print(board.move_row([3, 0, 0, 1]))
    print(board.move_row([1, 2, 0, 0]))
    print(board.move_row([0, 0, 1, 2]))
    print(board.move_row([0, 0, 0, 0]))
    print(board.move_row([1, 1, 1, 1]))
    