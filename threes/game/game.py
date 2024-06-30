import sys
import os
import numpy as np 

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from threes.board import Board
from threes.game_enums import MoveDirection, GameState

#TODO: tests
class Game:
    def __init__(self):
        self.board = Board()
        self.score = 0
        self.state = GameState.GAME_INIT
        self.next_tile = 0
        self.nr_moves = 0 
        
    def start(self):
        self.board.init_board()
        self.generate_new_next_tile()
        self.score = 0
        self.nr_moves = 0
        self.state = GameState.GAME_RUNNING
    
    def move(self, direction: MoveDirection):
        new_board = self.board.move_board(direction)
        self.board.tiles = self.board.insert_new_tile(new_board, self.next_tile)
        self.generate_new_next_tile()
    
    def get_score(self):
        self.score = np.sum(self.board.tiles)        
        return self.score
    
    def generate_new_next_tile(self):
        possible_tiles, _ = self.get_tiles([], np.max(self.board.tiles))
        self.next_tile = np.random.choice(possible_tiles)
        
    
    def get_tiles(self, current_tiles, max_tile):
        if max_tile <= 3:
            current_tiles.append(1)
            current_tiles.append(2)
        else:
            current_tiles.append(int(max_tile/2))
            self.get_tiles(current_tiles, max_tile/2)
            
        return current_tiles, max_tile
        
    
    def available_moves(self):
        avaliable_moves = []
        
        for direction in MoveDirection:
            new_board = self.board.move_board(direction)
            if not np.array_equal(new_board, self.board.tiles):
                avaliable_moves.append(direction)
        
        return avaliable_moves


if __name__ == "__main__":
    game = Game()
    
    game.start()
    game.move(MoveDirection.UP)
    game.get_score()
    