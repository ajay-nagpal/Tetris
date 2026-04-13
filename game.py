#to better organise and manage the game structure, imp things keep centralize
from grid import Grid
from blocks import *
import random 

class Game:
    def __init__(self):
        #gmae class must create and hold the grid
        self.grid=Grid()
        #same for block, but select random block
        self.blocks=[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]

        self.current_block=self.get_random_block()
        self.next_block=self.get_random_block()


    def get_random_block(self):
        #let each of the 7 blocks appear at least once before random appearance
        if len(self.blocks)==0:
            self.blocks=[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]

        block=random.choice(self.blocks)
        self.blocks.remove(block)# next time it won't appear
        return block
        #when list becomes empty refill the lsit will alll the blocks again so cehck it first
        #after all these we can create current and next block  in __init__

    #this should have draw methods to draw on the screen
    def draw_game(self,screen):
        self.grid.draw_grid(screen)
        self.current_block.draw_block(screen)

    def move_left(self):
        self.current_block.move(0,-1)#row,col, col will decrease, y,x, x-- left movement
        if not self.is_block_inside():
            #move back
            self.current_block.move(0,1)

    def move_right(self):
        self.current_block.move(0,1)#row,col,
        if not self.is_block_inside():
            #move back
            self.current_block.move(0,-1)
    
    def move_down(self):
        self.current_block.move(1,0)#row,col, 
        if not self.is_block_inside():
            #move back
            self.current_block.move(-1,0)

    def is_block_inside(self):
        #first get list of tiles
        tiles=self.current_block.get_cell_positions()

        for tile in tiles:
            if not self.grid.is_inside_grid(tile.rows,tile.cols):
                return False
        return True
    
    def rotate(self):
        self.current_block.rotate()
        if not self.is_block_inside():
            self.current_block.undo_rotate()

