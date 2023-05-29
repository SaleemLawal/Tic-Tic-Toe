import pygame
from Game import Game
DIMENSION = (770, 770)


def addXO(game, position):
    locations = [0, DIMENSION[0]//3, (DIMENSION[0]//3) *2]
    x, y = position[0], position[1]
    curr_img = pygame.image.load(f"assets/{game.current_player}.png")
    game.updateTable(x, y)
    game.checkTable()
    screen.blit(curr_img, (x, y))
    game.togglePlayer()


def updateBoard(bool, game, mouse_position):
    if bool:
        addXO(game, mouse_position)
    pygame.display.flip()
    
if __name__ == '__main__':
    mouse_position = (0,0)
    #pygame setup
    pygame.init()
    pygame.display.set_caption("Tic Tac Toe")
    screen = pygame.display.set_mode(DIMENSION)
    screen.fill(color=(216, 191, 216))
    board = pygame.image.load("assets/Board.png")
    screen.blit(source= board, dest=(0,0))
    
    # TicTacToe
    game = Game()
    while True:
        # game.checkTable()
        clicked = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                clicked = True
                mouse_position = pygame.mouse.get_pos()
                print(mouse_position)
        updateBoard(clicked, game, mouse_position)
        
