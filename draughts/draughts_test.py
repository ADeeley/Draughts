from draughts import *
import unittest

class test_board_methods(unittest.TestCase):

    def test_place_counters(self):
        b = Board()
        board = b.place_counters()
        self.assertEqual(len(b.tiles),  64)

    def test_get_tile(self):
        b = Board()
        self.assertEqual(b.get_tile("A1"), None)
        self.assertEqual(b.get_tile("H8"), None)
       
    def test_place_counters(self):
        b = Board()
        b.place_counters()
        starting_spaces = ['A2', 'A4', 'A6', 'A8', 'B1', 'B3', 'B5', 'B7', 
        'C2', 'C4', 'C6', 'C8', 'F1', 'F3', 'F5', 'F7',  
        'G2', 'G4', 'G6', 'G8', 'H1', 'H3', 'H5', 'H7']
        for space in starting_spaces[0:12]:
            self.assertEqual(b.tiles[space] .get_location(), space)
            self.assertEqual(b.tiles[space].get_colour(), "R")
        
        for space in starting_spaces[12:]:
            self.assertEqual(b.tiles[space] .get_location(), space)
            self.assertEqual(b.tiles[space].get_colour(), "B")

    def test_move_counter(self):     
        b = Board()
        b.place_counters()
        b.move_counter("C2", "D3")
        self.assertEqual(b.get_tile("C2"), None)
        self.assertNotEqual(b.get_tile("D3"), None)
        
    def test_is_legal_move(self):
        pass
        
        
            
class test_counter_methods(unittest.TestCase):

    def test_counter(self):
        counter = Counter("A1", "R")     
        self.assertEqual(counter.get_colour(),  "R")
        self.assertEqual(counter.get_location(), "A1")
        
        
class test_player_methods(unittest.TestCase):    
    ''' A class to keep track of the wins and losses for each player. '''

    def test_get_wins(self):
        p = Player()
        self.assertEqual(p.get_wins(), 0)
        for iter in range(5):
            p.add_win()
        
        self.assertEqual(p.get_wins(), 5)
       
    def test_get_losses(self):
        p = Player()
        self.assertEqual(p.get_losses(), 0)
        for iter in range(5):
            p.add_loss()
        
        self.assertEqual(p.get_losses(), 5)
           

if __name__ == '__main__':
    unittest.main()