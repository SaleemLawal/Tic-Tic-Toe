import pygame as pg
from random import randint  
DEFAULT_IMAGE_SIZE = (100, 100)
HEIGHT = 500
WIDTH = 500

class Logic():
    def __init__(self) -> None:
        self.win = False
        self.board = [[None]*3, [None]*3, [None]*3]
        self.players = ['X', 'O']
        
    def CheckWin(self):
        '''
          0  1  2
        0 x, x, x
        1 x, x, x
        2 x, x, x 
        '''
        # check wins in each row
        for row in range(0, 3):
            if ((self.board[row][0] == self.board[row][1] == self.board[row][2]) and self.board[row][0] is not None):
                self.win = True
                break
        # check win in each column
        for col in range(0, 3):
            if ((self.board[0][col] == self.board[1][col] == self.board[2][col]) and self.board[0][col] is not None):
                self.win = True
                break
        #check win diagonally
        if (((self.board[0][0] == self.board[1][1] == self.board[2][2]) or (self.board[0][2] == self.board[1][1] == self.board[2][0])) 
            and self.board[1][1] is not None):
            self.win = True
            
    def turn(self):
        num = randint(0, 1)
        if num == 0:
            pg.display.set_caption(f"{self.players[0]} Goes first")
        else:
            pg.display.set_caption(f'{self.players[1]} Goes first')



def initialize_screen():
    """
        Creates the screen and draws the demarcating lines, 
        updates the screen while the game is ongoing
    """
    width_sec = WIDTH//3
    height_sec = HEIGHT//3
    demarcation = [(width_sec, 0), (width_sec, HEIGHT), (width_sec * 2, HEIGHT), 
                   (width_sec * 2, 0), (0, 0), (0, height_sec), (WIDTH,height_sec), (WIDTH, height_sec*2), (0, height_sec*2)] 
    screen.fill("white")
    pg.draw.lines(surface=screen, color="black", closed= False, points=demarcation)

    for pos in positions:
        print(pos)
        screen.blit(o_symbol, pos)
    pg.display.flip()
    
    
if __name__ == '__main__':
    positions = []
    game_play = True
    
    pg.init()
    pg.display.set_caption('Tic Tac Toe')
    screen = pg.display.set_mode(size=(WIDTH,HEIGHT))
    x_symbol = pg.image.load("x.png")
    x_symbol = pg.transform.scale(x_symbol, DEFAULT_IMAGE_SIZE)
    o_symbol = pg.image.load("o.png")
    o_symbol = pg.transform.scale(o_symbol, DEFAULT_IMAGE_SIZE)
    
    while game_play:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                positions.append(event.pos)
                
            if event.type == pg.QUIT:
                game_play = False
        initialize_screen() 

   
    pg.quit()    
        

