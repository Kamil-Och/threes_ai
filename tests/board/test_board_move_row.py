import unittest
import sys
import os

sys.path.append("..")

from game.board.board import Board


class TestRowMove(unittest.TestCase):
    def setUp(self):
        self.threes = Board()
    
    def test_new_row_simple_move(self):
        new_row = self.threes.move_row([3, 0, 0, 1])
        self.assertEqual(new_row, [3, 0 , 1, -1])
        
    def test_new_row_simple_move_without_merge(self):
        new_row = self.threes.move_row([0, 0, 1, 2])
        self.assertEqual(new_row, [0, 1, 2, -1])
        
    def test_new_row_move_zeros(self):
        new_row = self.threes.move_row([0, 0, 0, 0])
        self.assertEqual(new_row, [0, 0, 0, -1])
        
    def test_new_row_simple_move_with_1_2_merge(self):
        new_row = self.threes.move_row([1, 2, 0, 0])
        self.assertEqual(new_row, [3, 0, 0, -1])
        
    def test_new_row_move_all_1(self):
        new_row = self.threes.move_row([1, 1, 1, 1])
        self.assertEqual(new_row, [1, 1, 1, 1])

if __name__ == '__main__':
    unittest.main()

