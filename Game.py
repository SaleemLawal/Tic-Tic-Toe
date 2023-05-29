class Game():
    def __init__(self) -> None:
        """default constructor
        """
        self.sections_found = []
        self.winner_found = False
        self.current_player = 'X'
        self.table = [[None] * 3 for i in range(3)]

    
    def togglePlayer(self):
        """toggles the other player after a player makes their move
        """
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        
    def TableFull(self):
        for row in self.table:
            for element in row:
                if element is None:
                    return False
        return True
                
    def checkWin(self):
        """checks after each player goes and checks for win

        Returns:
            _type_: returns a list containing the player if the game is won, 
                    and the player that won
        """
        winning_combinations = [
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(2, 0), (1, 1), (0, 2)]
        ]

        for combination in winning_combinations:
            symbols = [self.table[row][col] for row, col in combination]
            if symbols[0] is not None and all(symbol == symbols[0] for symbol in symbols):
                self.winner_found = True
                return self.winner_found
            
    
    def updateTable(self, x, y):
        """update table based on the coordinates passed in

        Args:
            x (int): affects the column axis
            y (int): affects the row axis
        """
        place_locations = [[(50,50), (320, 40), (590, 50)], 
                           [(50, 300), (320, 320), (590, 300)], 
                           [(50, 590), (320, 570), (590, 590)]]
        if x < 256:
            col = 0
        elif x < 512:
            col = 1
        else:
            col = 2
    
        if y < 256:
            row = 0
        elif y < 512:
            row = 1
        else:
            row = 2
            
        if (row,col) not in self.sections_found:
            self.table[row][col] = self.current_player
            self.sections_found.append((row, col)) 
            return True, place_locations[row][col]
        return False, 0
        