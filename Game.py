class Game():
    def __init__(self) -> None:
        # self.player = ['X', 'O']
        self.winner_found = False
        self.current_player = 'X'
        self.table = [ [None] * 3 ] * 3

    
    def togglePlayer(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        # print(self.current_player)
    
    
    def checkTable(self):
        print(self.table)

        
    def checkWin(self):
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
                return [self.winner_found, symbols[0]]
        return [False]
        # if (self.table[0][0] == self.table[1][0] == self.table[2][0]):
        #     print('X win')
        # elif (self.table[0][1] == self.table[1][1] == self.table[2][1]):
        #     print()
        # elif (self.table[0][2] == self.table[1][2] == self.table[2][2]):
        #     print()
        # elif (self.table[0][0] == self.table[0][1] == self.table[0][2]):
        #     print()
        # elif (self.table[1][0] == self.table[1][1] == self.table[1][2]):
        #     print()
        # elif (self.table[2][0] == self.table[2][1] == self.table[2][2]):
        #     print()
        # elif (self.table[0][0] == self.table[1][1] == self.table[2][2]):
        #     print()
        # elif (self.table[2][0] == self.table[1][1] == self.table[0][2]):
        #     print()
        if None not in self.table and not(self.winner_found):
            print("DRAW")
            
    
    def updateTable(self, x, y):
        print(x, y)
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
        self.table[row][col] = self.current_player
        