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
       
    def test_move_counter(self):     
        b = Board()
        b.place_counters()
        b.move_counter("C2", "D3")
        self.assertEqual(b.get_tile("C2"), None)
        self.assertNotEqual(b.get_tile("D3"), None)
        
    def test_get_diagonal(self):
        b = Board()
        self.assertEqual(b.get_diagonal("F1", "G2"), ["F1", "G2", "H3"])
        self.assertEqual(b.get_diagonal("B1", "H7"), ["B1", "C2", "D3", "E4", "F5", "G6", "H7"])
        self.assertEqual(b.get_diagonal("G8", "H7"), ["G8", "H7"])
        self.assertFalse(b.get_diagonal("A1", "R8"))
        self.assertFalse(b.get_diagonal("J7", "H2"))
        self.assertFalse(b.get_diagonal("J7", "T8"))
        self.assertFalse(b.get_diagonal("J7", "T8"))
        
    def test_get_movement_distance(self):
        b = Board()
        self.assertEqual(b.get_movement_distance("F1", "G2"), 1)
        self.assertEqual(b.get_movement_distance("B1", "D3"), 2)
        self.assertEqual(b.get_movement_distance("A8", "H1"), 7)
        self.assertEqual(b.get_movement_distance("E8", "H5"), 3)
        
    def test_get_intermediate_tile_reference(self):
        b = Board()
        self.assertEqual(b.get_intermediate_tile_reference("F1", "H3"), "G2")
        self.assertEqual(b.get_intermediate_tile_reference("B1", "D3"), "C2")
        self.assertEqual(b.get_intermediate_tile_reference("E8", "G6"), "F7")
        
    def test_place_counters(self):
        b = Board()
        b.place_counters()
        starting_spaces = ['A2', 'A4', 'A6', 'A8', 'B1', 'B3', 'B5', 'B7', 
        'C2', 'C4', 'C6', 'C8', 'F1', 'F3', 'F5', 'F7',  
        'G2', 'G4', 'G6', 'G8', 'H1', 'H3', 'H5', 'H7']
        for space in starting_spaces[0:12]:
            self.assertEqual(b.tiles[space] .get_location(), space)
            self.assertEqual(b.tiles[space].get_colour(), "Red")
        
        for space in starting_spaces[12:]:
            self.assertEqual(b.tiles[space] .get_location(), space)
            self.assertEqual(b.tiles[space].get_colour(), "Black")

    def test_is_legal_move(self):
        b = Board()
        b.place_counters()
        self.assertFalse(b.is_legal_move("C2", "C2", "Red"))
        self.assertFalse(b.is_legal_move("A6", "B7", "Red"))
        self.assertFalse(b.is_legal_move("F5", "G5", "Black"))
        self.assertFalse(b.is_legal_move("C6", "E4", "Red"))
        self.assertFalse(b.is_legal_move("A8", "C5", "Red"))
        self.assertFalse(b.is_legal_move("C8", "E1", "Red"))
        self.assertFalse(b.is_legal_move("C2", "D3", "Black"))
        self.assertFalse(b.is_legal_move("F3", "E4", "Red"))
        
        self.assertTrue(b.is_legal_move("C4", "D5", "Red"))
        self.assertTrue(b.is_legal_move("C8", "D7", "Red"))
        b.move_counter("C2", "D3")
        b.move_counter("F1", "E2")
        self.assertTrue(b.is_legal_move("D3", "F1", "Red"))

        
class test_counter_methods(unittest.TestCase):

    def test_counter(self):
        counter = Counter("A1","R", "Red")     
        self.assertEqual(counter.get_colour(),  "Red")
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