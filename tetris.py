import pygame
init_module=pygame.init()

#set display size
game_window=pygame.display.set_mode((1080,1080))

#set title
pygame.display.set_caption("T£tr!$")

#set game specific variables
#to exit the game, wehn true game quit
exit_game=False

#similerly for game over
game_over=False 

# fix game window 
# and to take actions during game,
# use  game loop