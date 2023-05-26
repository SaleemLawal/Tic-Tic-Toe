import pygame as pg
from random import randint  


def initialize_screen():
    screen.fill("white")
    pg.display.flip()
    
if __name__ == '__main__':
    game_play = True
    pg.init()
    screen = pg.display.set_mode(size=(700,700))
    
    while game_play:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_play = False
        initialize_screen()        
         
    pg.quit()    
        

