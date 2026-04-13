import pygame,sys
from game import Game 

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


#block.move(4,3)
# fix game window 
# and to take actions during game,
# use  game loop
game=Game()

GAME_UPDATE=pygame.USEREVENT#to create custom events, llike slow moving down of a block
#we will use it for block position update 
pygame.time.set_timer(GAME_UPDATE,300)#300 milisecod move do2nw time instead of 60fpc

while not exit_game:
#handle events
    for event in pygame.event.get():
        # print(event)
        #handle quit event
        if event.type==pygame.QUIT:
            exit_game=True
            break

        #handle keypress event
        if event.type==pygame.KEYDOWN:
            #which key
            if event.key==pygame.K_LEFT:
                #move block to the left
                #create move_left() in game class to encapsulate things
                game.move_left()
            elif event.key==pygame.K_RIGHT:
                game.move_right()
            elif event.key==pygame.K_DOWN:
                game.move_down()
            
            elif event.key==pygame.K_UP:#rotate bklock
                #block might go out of bound
                game.rotate()
                #handle that too

            #check bounmdry, cehck if tile is inside grid, create a menhod for that in grid
        
        #cehck for custom event
        if event.type==GAME_UPDATE:
            game.move_down()
            # if reached bottom, still ewe can move it , fix this issue
            #create lock block method call it in move down
         
        
        game_screen.fill(dark_grey_blue)

        #draw the screen
        #game_grid.draw_grid(game_screen) #use game class
        #this will show again blank , bcz currently all zeros and no margin 
        #to amek cell visible add margin of 1 pixel to each cell, cell size is 40*40 pixels
        #so we can draw a 39*39 pixel grey rectangelor each cell

        # to make this work
        # add 1 pixel offset at x and y pos of cell_rect in grid
        # also substract 1 pixel from the w and h of cell_rect we draw in grid.py

        #draw the block
        #block.draw_block(game_screen)
        game.draw_game(game_screen)

        #move down automatically but not as fast as 60fps, slow down speed
        #game.move_down()  removed handled using custom event 

        pygame.display.update()
        #let play in 60 fps
        clock.tick(60)

        #color format (r,g,b)=> 0: that color not present at all

        

#quit pygame
pygame.quit()

sys.exit()