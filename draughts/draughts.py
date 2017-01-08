class Board():

    def  __init__(self):
        rows = "ABCDEFGH"
        cols = "12345678"
        tileNames = [x+y for x in rows for y in cols]
        self.tiles = dict([x, None] for x in tileNames )
        assert len(self.tiles) == 64
        
    def setup_board(self):
        '''Sets up a draughts board with the pieces in the starting positions
        - returns dictionary board with references A1 to H8
        - to add'''
        rows = "ABCDEFGH"
        cols = "12345678"
        tileNames = [x+y for x in rows for y in cols]
        tiles = dict([x, None] for x in tileNames )
        assert len(tiles) == 64
        return tiles
    
    def place_counters(self):
        ''' Places the counters on the board for red and black.
            - returns nothing '''
        starting_spaces = ['A2', 'A4', 'A6', 'A8', 'B1', 'B3', 'B5', 'B7', 
        'C1', 'C3', 'C5', 'C7', 'F1', 'F3', 'F5', 'F7',  
        'G2', 'G4', 'G6', 'G8', 'H1', 'H3', 'H5', 'H7']
        
        for tile in starting_spaces[0:12]:
            self.tiles[tile] = Counter(tile, "Red")
    
        for tile in starting_spaces[12:]:
            self.tiles[tile] = Counter(tile, "Black")
            
    def get_tile(self, tile):
        return self.tiles[tile]
        
class Counter():
    
    def __init__(self,  location, colour):
        self.location = location
        self.colour = colour
        
    def get_colour(self):
        ''' Returns a string (Red or Black) of the colour of the counter.'''
        return self.colour
        
    def  get_location(self):
        ''' Returns a string of the location of the counter e.g. "A1" '''
        return self.location