import pygame,sys
from grid import Grid
#import block
from blocks import *

init_module=pygame.init()
#set display size
game_screen=pygame.display.set_mode((480,800))

#set title
pygame.display.set_caption("T£tr!$")

#create a clock obj to control the frame rate of the game
#i.e.  how fast the game will run
clock=pygame.time.Clock()

dark_grey_blue=(62, 68, 81)#(26,31,41)#light grey

#set game specific variables
#to exit the game, wehn true game quit
exit_game=False
#similerly for game over
game_over=False 
game_grid=Grid()

#lets create Lblock for testing
block=IBlock()

# fix game window 
# and to take actions during game,
# use  game loop

while not exit_game:
#handle events
    for event in pygame.event.get():
        # print(event)
        #handle quit event
        if event.type==pygame.QUIT:
            exit_game=True
            break
        
        game_screen.fill(dark_grey_blue)

        #draw the screen
        game_grid.draw_grid(game_screen)
        #this will show again blank , bcz currently all zeros and no margin 
        #to amek cell visible add margin of 1 pixel to each cell, cell size is 40*40 pixels
        #so we can draw a 39*39 pixel grey rectangelor each cell

        # to make this work
        # add 1 pixel offset at x and y pos of cell_rect in grid
        # also substract 1 pixel from the w and h of cell_rect we draw in grid.py

        #draw the block
        block.draw(game_screen)

        pygame.display.update()
        #let play in 60 fps
        clock.tick(60)

        #color format (r,g,b)=> 0: that color not present at all

        #handle keypress event
        if event.type==pygame.KEYDOWN:
            pass
            #which key
            # if event.key==pygame.K_RIGHT:#let right arrow key
            #    print("right arrow key pressed")
            #will use when moveing things
         

#quit pygame
pygame.quit()

sys.exit()