import pygame
from Game import Game
DIMENSION = (770, 770)


def addXO(game, position, screen):
    """add either an X or O at the mouse clicked location,
        depending ton the current player
    Args:
        game (Class): class object that holds functions related to the game functionability
        position (tuple):  x and y coordinates of where the player clicked
    """
    x, y = position[0], position[1]
    # checks if position isnt occupied, if it isnt, it place the player at a symbol at a position place_at_location
    valid, place_at_location = game.updateTable(x, y)
    
    if valid:
        curr_img = pygame.image.load(f"assets/{game.current_player}.png")
        screen.blit(curr_img, place_at_location)
        game.togglePlayer()
        pygame.display.set_caption(f"{game.current_player} turn, Aggregate x: {X_wins} y: {O_wins}")


def updateBoard(bool, game, mouse_position, screen):
    """updates changes made to the board

    Args:
        bool (boolean): True is passed when the mouse is clicked 
        game (object): contains the object with the game functionality
        mouse_position (tuple): x and y coordinates of where the player clicked
    """
    if bool:
        addXO(game, mouse_position, screen)
    pygame.display.flip()


def screen_intialization():
    #pygame setup
    pygame.display.set_caption(f"Tic Tac Toe, Aggregate x: {X_wins} y: {O_wins}")
    screen = pygame.display.set_mode(DIMENSION)
    screen.fill(color=(216, 191, 216))
    board = pygame.image.load("assets/Board.png")
    screen.blit(source= board, dest=(0,0))
    return screen
        
        
def main():
    global X_wins, O_wins
    pygame.init()
    mouse_position = (0,0)
    game = Game()
    done = False
    screen = screen_intialization()
    
     # TicTacToe
    while not done:
        clicked = False
        win, positions, player_won = game.checkWin()
        
        if win:
            for pos in positions:
                curr_img = pygame.image.load(f"assets/Winning_{player_won}.png")
                screen.blit(curr_img, pos)
                pygame.display.flip()
            if player_won == 'X':
                X_wins += 1
            else:
                O_wins += 1
            pygame.time.delay(500)   
        elif game.TableFull():
            pygame.display.set_caption("Draw")
            
        # keeps the game running
        if win or game.TableFull():
            game = Game() 
            screen = screen_intialization()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONUP:
                clicked = True
                mouse_position = pygame.mouse.get_pos()
                print(mouse_position)
        updateBoard(clicked, game, mouse_position, screen)
        

if __name__ == '__main__': 
    X_wins = 0
    O_wins = 0
    main()
    
