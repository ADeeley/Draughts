from draughts import *
import unittest

class test_board_methods(unittest.TestCase):

    def test_setup_board(self):
        b = Board()
        board = b.setup_board()
        self.assertEqual(len(board),  64)

    def test_get_tile(self):
        b = Board()
        self.assertEqual(b.get_tile("A1"), None)
        self.assertEqual(b.get_tile("H8"), None)
       
    def test_place_counters(self):
        b = Board()
        b.place_counters()
        starting_spaces = ['A2', 'A4', 'A6', 'A8', 'B1', 'B3', 'B5', 'B7', 
        'C1', 'C3', 'C5', 'C7', 'F1', 'F3', 'F5', 'F7',  
        'G2', 'G4', 'G6', 'G8', 'H1', 'H3', 'H5', 'H7']
        for space in starting_spaces[0:12]:
            self.assertEqual(b.tiles[space] .get_location(), space)
            self.assertEqual(b.tiles[space].get_colour(), "Red")
        
        for space in starting_spaces[12:]:
            self.assertEqual(b.tiles[space] .get_location(), space)
            self.assertEqual(b.tiles[space].get_colour(), "Black")
            
class test_counter_methods(unittest.TestCase):

    def test_counter(self):
        counter = Counter("A1", "Red")     
        self.assertEqual(counter.get_colour(),  "Red")
        self.assertEqual(counter.get_location(), "A1")
        
if __name__ == '__main__':
    unittest.main()