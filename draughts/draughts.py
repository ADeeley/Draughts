class Board():
    ''' Sets up a blank draughts board'''
    def  __init__(self):
        rows = "ABCDEFGH"
        cols = "12345678"
        self.tileNames = [x+y for x in rows for y in cols]
        self.tiles = dict([x, None] for x in self.tileNames )
        assert len(self.tiles) == 64
    
    def place_counters(self):
        ''' Places the counters on the board for red and black.
            - returns nothing '''
        starting_spaces = ['A2', 'A4', 'A6', 'A8', 'B1', 'B3', 'B5', 'B7', 
        'C2', 'C4', 'C6', 'C8', 'F1', 'F3', 'F5', 'F7',  
        'G2', 'G4', 'G6', 'G8', 'H1', 'H3', 'H5', 'H7']
        
        for tile in starting_spaces[0:12]:
            self.tiles[tile] = Counter(tile, "R")
    
        for tile in starting_spaces[12:]:
            self.tiles[tile] = Counter(tile, "B")
            
    def display_board(self):
        counter = 0
        for tile in self.tileNames:
            if counter %8 == 0:
                print("\n")
            if self.tiles[tile] != None:
                print(self.tiles[tile].get_colour(), end=", ")
            else:
            
                print(".", end=", ")
            counter += 1
    
    def get_tile(self, tile):
        if self.tiles[tile]:
            return self.tiles[tile]
        else:
            return None
        
    def move_counter(self, source, destination):
        ''' Moves the counter if the destination tile is free. '''
        if self.tiles[source] and not self.tiles[destination]:
            temp = self.tiles[source]
            self.tiles[source] = None
            self.tiles[destination] = temp
        else:
            print("Invalid move!")
        
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

        
class Player1():    
    def __init__(self):
        pass
        
class Player1():    
    def __init__(self):
        pass