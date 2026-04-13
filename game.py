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

        self.game_over=False


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
        if not self.is_block_inside() or not self.block_fits():
            #move back
            self.current_block.move(0,1)

    def move_right(self):
        self.current_block.move(0,1)#row,col,
        if not self.is_block_inside() or not self.block_fits():
            #move back
            self.current_block.move(0,-1)
    
    def move_down(self):
        self.current_block.move(1,0)#row,col, 
        if not self.is_block_inside() or not self.block_fits():#but what about move left right etc
            #move back
            self.current_block.move(-1,0)
            self.lock_block()
            #locked but blocks overriding each other fix that
            #simply cehck if cells , that block occupies are empty or not 
            #if not empty undo the move, lock the block in place on grid
            ##means
            #block should be on empty cell of he grid, not occupied cell
            #create is_empty in grid
            
    def lock_block(self):
        # get all tiles of block
        tiles=self.current_block.get_cell_positions()
        #for each cell position we will store id of a block in the grid
        for position in tiles:
            self.grid.grid[position.row][position.col]=self.current_block.id
        #now new blokc on the screen once current reaches final point
        self.current_block=self.next_block
        #update next block with random block
        self.next_block=self.get_random_block()
        #clear row if any needed
        self.grid.clear_full_rows()

        #if the new block fits in the screen,  if not fit means overlap with other block
        #then game over
        if not self.block_fits():
            self.game_over=True 
            #now stop updating game in every 300 ms



    def block_fits(self):
        tiles=self.current_block.get_cell_positions()
        for tile in tiles:
            #cehck if any tile is occupied
            if not self.grid.is_empty(tile.row,tile.col):
                return False
        return True#block can mopve to specified position


    def is_block_inside(self):
        #first get list of tiles
        tiles=self.current_block.get_cell_positions()

        for tile in tiles:
            if not self.grid.is_inside_grid(tile.row,tile.col):
                return False
        return True
    
    def rotate(self):
        self.current_block.rotate()
        if not self.is_block_inside() or not self.block_fits():
            self.current_block.undo_rotate()


    def reset(self):
        self.grid.reset()
        #create a list of all theblocks , assign current and next a random one
        self.blocks=[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.current_block=self.get_random_block()
        self.next_block=self.get_random_block()
