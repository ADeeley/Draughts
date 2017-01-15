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
            self.tiles[tile] = Counter(tile, "R", "Red")
    
        for tile in starting_spaces[12:]:
            self.tiles[tile] = Counter(tile, "B", "Black")
            
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
                print(self.tiles[tile].get_display_name(), end="  ")
            else:
            
                print(". ", end=" ")
            counter += 1
        print("| ", letters[-1   ], "\n\t -------------------------\n\t  1, 2, 3, 4, 5, 6, 7, 8\n ")
    
    def get_tile(self, tile):
        if self.tiles[tile]:
            return self.tiles[tile]
        else:
            return None
           
    def move_counter(self, source, destination):
        ''' Moves the counter if the destination tile is free. '''
        source = source.upper()
        destination = destination.upper()
        if source not in self.tiles or destination not in self.tiles:
            print("\tInvalid move!")
        elif self.tiles[source] and not self.tiles[destination]:
            temp = self.tiles[source]
            self.tiles[source] = None
            self.tiles[destination] = temp
        else:
            print("\tInvalid move!")
       
    def get_diagonal(self, source, destination):
        ''' Returns the diagonal list which includes both source and desination tiles'''
        for diagonal in self.diagonals:
            if source in diagonal and destination in diagonal:
                return diagonal
        return False
               
    def movementDistance(self, source, destination):
        diagonal = self.get_diagonal(source, destination)
        if diagonal == False:
            return False
        movementDistance = abs(diagonal.index(source) - diagonal.index(destination))
        return movementDistance
     
    def get_intermediate_tile_reference(self, source, destination):
        diagonal = self.get_diagonal(source, destination)
        if diagonal == False:
            return False
            
        intermediateTile = abs(diagonal.index(source) + diagonal.index(destination)) / 2
        refIntermediateTile = diagonal[int(intermediateTile)]
        return refIntermediateTile
        
    def check_and_take_tiles(self, source, destination):
        
        intermediateTile = self.get_intermediate_tile_reference(source, destination)
        if self.tiles[intermediateTile]:
            self.tiles[intermediateTile] = None
     
    def is_legal_move(self, source, destination, playerColour):
        '''Returns True if the move is valid and False otherwise.'''
        # Check if the tile references are on the board
        if source not in self.tiles:
            print("\tSource tile not on board.")
            return False
        elif destination not in self.tiles:
            print("\tDestination tile not on board.")
            return False
        # Check if the source and destination tiles are the same reference
        elif source == destination:
            print("\tSource tile is the same as the destination tile.")
        # Check if there is a tile on the source tile and the desination tile is empty
        elif not self.tiles[source]:
            print("\tThere is no counter on source location %s" % source)
            return False
        elif self.tiles[destination]:
            print("\tThere is already a counter on location %s" % source)            
            return False
        # Check if the play is moving one of his own coloured counters
        elif self.tiles[source].get_colour() != playerColour:
            print("\tYou are %s. You can't move your opponent's counters" %playerColour)
            return False        
        # check if the play is trying to move backwards
        rows = "ABCDEFGH"
        if self.tiles[source].get_colour() == "Red":
            if rows.index(destination[0]) < rows.index(source[0]):
                print("\tCan't move backwards, fool.")
                return False
        elif self.tiles[source].get_colour() == "Black":
            if rows.index(destination[0]) > rows.index(source[0]):
                print("\tCan't move backwards, fool.")
                return False
        # check the distance between source tile and destination tile
        movementDistance = self.movementDistance(source, destination)
        
        if movementDistance == 0:
            print("\tInvalid Move")
            return False
        elif movementDistance ==1:
            if self.tiles[destination] != None:
                print("\tInvalid Move")            
                return False
        elif movementDistance == 2:
            intermediateTile = self.get_intermediate_tile_reference(source, destination)
            if not self.tiles[intermediateTile]:
                print("\tInvalid Move")
                return False
        elif movementDistance > 2:
            print("\tInvalid Move")
            return False
        
        return True
        
class Counter():    
    def __init__(self,  location, display_name, colour):
        self.location = location
        self.colour = colour
        self.display_name = display_name
        
    def get_colour(self):
        ''' Returns a string (Red or Black) of the colour of the counter.'''
        return self.colour
    def get_display_name(self):
        return self.display_name
        
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
        self.numberOfCountersOnBoard = 12
    
    def get_wins(self):
        return self.wins
        
    def get_losses(self):
        return self.losses       
        
    def add_win(self):
        self.wins += 1
        
    def add_loss(self):
        self.losses += 1  
        
    def get_number_of_counters_on_board(self):
        return self.numberOfCountersOnBoard
        
        
class PlayGame():
    def __init__(self):
        self.game_over = False
        self.player1 = Player()
        self.player2 = Player()
        
    def check_if_game_over(self):
        ''' Checks if game over is True and prints out the winning player '''  
        player1Counters = self.player1.get_number_of_counters_on_board()
        player2Counters = self.player2.get_number_of_counters_on_board()
        if player1Counters == 0:
            print("Player2 wins!")
            self.game_over = True
        elif player1Counters == 0:
            print("Player1 wins!")
            self.game_over = True
            
    def get_user_input(self, colour):
        ''' Gets the user input and ensures this is in the format x1, y1. 
            - Returns the input as two strings, source and destination. '''
        while True:
            userInput = input("\t%s move: " % colour).split()
            if not len(userInput) == 2:
                print("\tSorry, that command is not recognised. Moves must be in the format x1 y1")
                continue
            else:
                source = userInput[0].upper()
                destination = userInput[1].upper()
            if len(source) == 2 and len(destination) == 2:                    
                return source, destination
            else:
                print("\tSorry, that command is not recognised. Moves must be in the format x1 y1")
                
    def start_game(self):
        ''' Manages the game loop and resets the board '''
        moves = 0
        game = Board()
        game.place_counters()
        if self.game_over:
            self.game_over = False

        print("""
 @@@@  @@@@    @@@  @   @  @@@  @   @ @@@@@  @@@@
 @   @ @   @  @   @ @   @ @   @ @   @   @   @
 @   @ @@@@   @@@@@ @   @ @ @@@ @@@@@   @    @@@
 @   @ @  @   @   @ @   @ @   @ @   @   @       @
 @@@@  @   @  @   @  @@@   @@@  @   @   @   @@@@
 
 by Adam M Deeley.""")
        # --------------- main game loop -------------------
        while not self.game_over:
            if moves % 2 == 0:
                colour = "Red"
            else:
                colour = "Black"
            
            game.display_board()
            source, destination = self.get_user_input(colour)
            if game.is_legal_move(source, destination, colour):
                game.move_counter(source, destination)
                if game.movementDistance(source, destination) == 2:
                    game.check_and_take_tiles(source, destination)
                    
                moves += 1
                self.check_if_game_over()
            else:
                continue
        
            
if __name__ == '__main__':            
    game = PlayGame()
    game.start_game()


