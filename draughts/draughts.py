class Board():
    ''' Sets up a blank draughts board'''
    def  __init__(self):
        rows = "ABCDEFGH"
        cols = "12345678"
        self.tileNames = [x+y for x in rows for y in cols]
        self.tiles = dict([x, None] for x in self.tileNames )
        assert len(self.tiles) == 64
        self.diagonals = [["F1", "G2", "H3"], ["D1", "E2", "F3", "G4", "H5"],  
                                  ["B1", "C2", "D3", "E4", "F5", "G6", "H7"], 
                                  ["A2", "B3", "C4", "D5", "E6", "F7", "G8"], 
                                  ["A4", "B5", "C6", "D7", "E8"], ["A6", "B7", "C8"], 
                                  ["A2", "B1"], ["A4", "B3", "C2", "D1"],
                                  ["A6", "B5", "C4", "D3", "E2", "F1"],
                                  ["A8", "B7", "C6", "D5", "E4", "F3", "G2", "H1"],
                                  ["C8", "D7", "E6", "F5", "G4", "H3"],
                                  ["E8", "F7", "G6", "H5"],
                                  ["G8", "H7"]]
        
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
        letters = "ABCDEFGH"
        counter = 0
        letter_counter = 0
        print("\n\t\t  \n\t -------------------------")
        for tile in self.tileNames:
            if counter %8 == 0 and counter != 0:
                print("| ", letters[letter_counter], "\n        |\t\t\t  |")
                letter_counter += 1
            if counter %8 == 0:
                print("\t| ", end="")
            if self.tiles[tile] != None:
                print(self.tiles[tile].get_colour(), end="  ")
            else:
            
                print(". ", end=" ")
            counter += 1
        print("|", letters[-1   ], "\n\t -------------------------\n\t  1, 2, 3, 4, 5, 6, 7, 8\n ")
    
    def get_tile(self, tile):
        if self.tiles[tile]:
            return self.tiles[tile]
        else:
            return None
        
    def move_counter(self, source, destination):
        ''' Moves the counter if the destination tile is free. '''
        source = source.upper()
        destination = destination.upper()
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

    def get_possible_moves(self):
        pass
        
class Player():    
    ''' A class to keep track of the wins and losses for each player. '''
    def __init__(self):
        self.wins = 0
        self.losses = 0
    
    def get_wins(self):
        return self.wins
        
    def get_losses(self):
        return self.losses       
        
    def add_win(self):
        self.wins += 1
        
    def add_loss(self):
        self.losses += 1  
        
class playGame():
    def __init__(self):
        self.game_over = False
    
    def start_game(self):
        moves = 0
        game = Board()
        game.place_counters()
        player1 = Player()
        player2 = Player()

        print("""
 @@@@  @@@@    @@@  @   @  @@@  @   @ @@@@@  @@@@
 @   @ @   @  @   @ @   @ @   @ @   @   @   @
 @   @ @@@@   @@@@@ @   @ @ @@@ @@@@@   @    @@@
 @   @ @  @   @   @ @   @ @   @ @   @   @       @
 @@@@  @   @  @   @  @@@   @@@  @   @   @   @@@@
 
 by Adam M Deeley.""")
        while not self.game_over:
            if moves % 2 == 0:
                player = "Red"
            else:
                player = "Black"
            
            game.display_board()
            src, dst = input("\t%s move: " % player).split()
            game.move_counter(src, dst)
            moves += 1
            
            
game = playGame()
game.start_game()


