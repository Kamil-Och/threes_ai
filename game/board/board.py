import numpy as np

class Board:
    def __init__(self, rows = 4, columns = 4, seed = None):
        self.tiles = np.zeros((rows, columns), dtype = np.int16)
        self.seed = seed
        self.rng = np.random.default_rng(self.seed)
        
    def init_board(self):
        
        initial_tiles = self.rng.choice(self.tiles.size, 9, replace = False)
        
        for i, _ in enumerate(self.tiles.flat):
            if i in initial_tiles:
                self.tiles.flat[i] = self.rng.choice([1, 2, 3])

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
    
    def insert_new_tile(self, board_tiles, value):
        #TODO: check if board_tiles is a numpy array
        
        indexes = []
        new_tiles_cords = np.where(board_tiles == -1)
        for tile_iter in range(len(new_tiles_cords[0])):
            indexes.append([new_tiles_cords[0][tile_iter], new_tiles_cords[1][tile_iter]])
            
        if len(indexes) == 0:
            return board_tiles

        for index in indexes:
            board_tiles[index[0], index[1]] = 0
        
        new_tile_index = self.rng.choice(indexes)
        board_tiles[new_tile_index[0], new_tile_index[1]] = value
        
        return board_tiles
    
    def move_board(self, direction):
        pass
    
    
    
    def sum_score(self, value):
        pass 
    
    
if __name__ == "__main__":
    board = Board()
    #print(board.board)
    # print(board.move_row([3, 0, 0, 1]))
    # print(board.move_row([1, 2, 0, 0]))
    # print(board.move_row([0, 0, 1, 2]))
    # print(board.move_row([0, 0, 0, 0]))
    # print(board.move_row([1, 1, 1, 1]))
    temp_board = np.array([[3, 0, 0, 1], 
                  [1, 2, 0, 0], 
                  [0, 0, 1, 2], 
                  [-1, 0, -1, 0]])
    
    print(board.insert_new_tile(temp_board, 1))
    
    