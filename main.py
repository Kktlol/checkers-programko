import pygame

#colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW   = ( 255, 255,   0)
TRANS    = (   1,   2,   3)

#Board
WIDTH = 800
HEIGHT = 800
players = ['x','o']
game_board =              [['x','-','x','-','x','-','x','-'],
						   ['-','x','-','x','-','x','-','x'],
			  			   ['x','-','x','-','x','-','x','-'],
						   ['-','-','-','-','-','-','-','-'],
						   ['-','-','-','-','-','-','-','-'],
						   ['-','o','-','o','-','o','-','o'],
						   ['o','-','o','-','o','-','o','-'],
						   ['-','o','-','o','-','o','-','o']]

# setup pygame
BOARD_SIZE = [8, 10, 12]
SCREEN_SIZE = (800, 800)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('blue')
    pygame.display.flip()
    clock.tick(60)

pygame.quit()