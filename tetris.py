import pygame,sys
from game import Game 
from color import Colors


init_module=pygame.init()
#set display size
game_screen=pygame.display.set_mode((780,800))

# for other game surface
title_font=pygame.font.Font(None,40)#None=>use default font, 40 size
#create a surface for the title
score_surface=title_font.render("Score",True,Colors.light_grey)#string that we want to display
#call block image transfer blit to make it appear on screen
#inside agame loop

#now create a rectangle obj to display score# dark grey color, light grey score
score_rect=pygame.Rect(540,55,170,100)

#same for title and others
next_surface=title_font.render("Next Block",True,Colors.light_grey)#string that we want to display
next_rect=pygame.Rect(520,320,210,190)


game_over_surface=title_font.render("Game Over",True,Colors.light_grey)#string that we want to display

#set title
pygame.display.set_caption("T£tr!$")

#create a clock obj to control the frame rate of the game
#i.e.  how fast the game will run
clock=pygame.time.Clock()


#set game specific variables
#to exit the game, wehn true game quit
exit_game=False
#will set  game over condition in Game 

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
            if game.game_over:
                game.game_over=False
                game.reset()
                
            #which key
            if event.key==pygame.K_LEFT and not game.game_over:
                #move block to the left
                #create move_left() in game class to encapsulate things
                game.move_left()
            elif event.key==pygame.K_RIGHT and not game.game_over:
                game.move_right()
            elif event.key==pygame.K_DOWN and not game.game_over:
                game.move_down()
                game.update_score(0,1)
            
            elif event.key==pygame.K_UP and not game.game_over:#rotate bklock
                #block might go out of bound
                game.rotate()
                #handle that too

            #check bounmdry, cehck if tile is inside grid, create a menhod for that in grid
        
        #cehck for custom event
        if event.type==GAME_UPDATE and not game.game_over:
            game.move_down()
            # if reached bottom, still ewe can move it , fix this issue
            #create lock block method call it in move down
         
        game_screen.fill(Colors.dark_grey_blue)
        
        game_screen.blit(score_surface,(590,20,50,50))
        pygame.draw.rect(game_screen,Colors.light_grey,score_rect,0,10)

        game_screen.blit(next_surface,(560,280,50,50))
        pygame.draw.rect(game_screen,Colors.light_grey,next_rect,0,10)

        if game.game_over:
            game_screen.blit(game_over_surface,(560,640,50,50))
        
        # created here cz score is dyn
        score_value_surface=title_font.render(str(game.score),True,Colors.dark_grey_blue)#string that we want to display
        #display score center of the surface
        game_screen.blit(score_value_surface,
                         score_value_surface.get_rect(centerx=score_rect.centerx,
                         centery=score_rect.centery))


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