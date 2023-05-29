import pygame
from Game import Game
DIMENSION = (770, 770)


def addXO(game, position):
    """add either an X or O at the mouse clicked location,
        depending ton the current player
    Args:
        game (Class): class object that holds functions related to the game functionability
        position (tuple):  x and y coordinates of where the player clicked
    """
    x, y = position[0], position[1]
    # checks if position isnt occupied, if it isnt,
    # it place the player at a symbol at a position place_at_location
    valid, place_at_location = game.updateTable(x, y)
    
    if valid:
        curr_img = pygame.image.load(f"assets/{game.current_player}.png")
        screen.blit(curr_img, place_at_location)
        game.togglePlayer()
        pygame.display.set_caption(f"{game.current_player} turn")

   


def updateBoard(bool, game, mouse_position):
    """updates changes made to the board

    Args:
        bool (boolean): True is passed when the mouse is clicked 
        game (object): contains the object with the game functionality
        mouse_position (tuple): x and y coordinates of where the player clicked
    """
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
        clicked = False
        if game.checkWin():
            exit()
        elif game.TableFull():
            print("DRAW")
            exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                clicked = True
                mouse_position = pygame.mouse.get_pos()
                print(mouse_position)

        updateBoard(clicked, game, mouse_position)
        
