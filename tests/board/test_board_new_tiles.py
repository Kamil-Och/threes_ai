import unittest
import sys
import os
import numpy as np

sys.path.append("..")

from game.board.board import Board

class TestNewTiles(unittest.TestCase):
    def setUp(self):
        self.threes = Board()
        
    def test_insert_new_tile_all_zeros(self):
        new_board = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        
        board = self.threes.insert_new_tile(new_board, 1)
        self.assertTrue(np.array_equal(board, new_board))
        
if __name__ == '__main__':
    unittest.main()