from color import Colors
import pygame

from position import Position

class Block:
    def __init__(self,id):
        self.id=id
        # this is going to be  dict
        #now we need to declare which cell are occupied
        #key will be rotation state(0 to 3)
        #value wil; be list , contiaing value of occupied cells
        self.cells={}
        self.cell_size=40
        self.rotation_state=0
        #block color, its same steps as in grid , so make it a class and use at other places
        self.colors=Colors.get_cell_colors();

        #for block movement create row and col offsets, 
        #let say form 0,0 to 5,3  move, we want to move a block
        #then row_offset=5+0, col_offset=3+0
        #movement is always downwards, so + for movement
        self.row_offset=0
        self.col_offset=0

    #method to draw on block, we need to know the surface we going to draw
    # in updated game later stage, we are showing next block that will apear on screen
    # so for drawing that too we will use this method
    #so we need 2 more parameters
    #offset_x, offset_y(offset things are related to next block in this method)
    def draw_block(self,screen,offset_x,offset_y):
        #we need the pos of each occupied ell of the block
        #in order to draw it on screen
        #create a new class named Position
        
        #this has now acccess to the rotation state of the blocks

        #self.cell is thjat specific block dect, let say L, then index it on totation state
        # to get that list of occccupied cells in a block for that L block

        # tiles=self.cells[self.rotation_state]
        #we created the get_cell_positons we can use that
        tiles=self.get_cell_positions()
        #now for each cell we can draw a rectangle using for loop

        for tile in tiles:
            #creaate a rectangle for each cell
            #pygame.Rect
            #same way we did in grid
            tile_rect=pygame.Rect(offset_x+tile.col*self.cell_size+1,offset_y+tile.row*self.cell_size+1,
                                  self.cell_size-1,self.cell_size-1)
            
            #now draw the cell
            pygame.draw.rect(screen,self.colors[self.id],tile_rect)


            #use this method to see the block on the screen

    def move(self,rows,cols):
        self.row_offset+=rows
        self.col_offset+=cols

    #this will return the position of the occupied cell, after applying the offsets
    #will apply the offset on corresponding list of that rotation status
    def get_cell_positions(self):
        #first get default cell pos for the current rotation state
        tiles=self.cells[self.rotation_state]
        #create a empty list to hold the move tile
        moved_tile=[]
        #loop through alll the tiles and add the offset to their position

        for position in tiles:
            position=Position(position.row+self.row_offset, position.col+self.col_offset)
            #append this new position to the moved_tile list
            moved_tile.append(position)

        return moved_tile
    
        # use this method in draw method to draw the updated position
        # we can use this get_cell_posiitons to get the tiles there


    def rotate(self):
        self.rotation_state+=1
        #it might go beyond range so check
        if self.rotation_state==len(self.cells):
            self.rotation_state=0

    #create a rotate method for game 

    def undo_rotate(self):
        self.rotation_state-=1
        #it might go beyond range so check
        if self.rotation_state==0:
            self.rotation_state=len(self.cells)-1


