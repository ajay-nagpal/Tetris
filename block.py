from color import Colors
import pygame

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

    #method to draw on block, we need to know the surface we going to draw
    def draw(self,screen):
        #we need the pos of each occupied ell of the block
        #in order to draw it on screen
        #create a new class named Position
        

        #this has now acccess to the rotation state of the blocks

        #self.cell is thjat specific block dect, let say L, then index it on totation state
        # to get that list of occccupied cells in a block for that L block

        tiles=self.cells[self.rotation_state]
        #now for each cell we can draw a rectangle using for loop

        for tile in tiles:
            #creaate a rectangle for each cell
            #pygame.Rect
            #same way we did in grid
            tile_rect=pygame.Rect(tile.cols*self.cell_size+1,tile.rows*self.cell_size+1,
                                  self.cell_size-1,self.cell_size-1)
            
            #now draw the cell
            pygame.draw.rect(screen,self.colors[self.id],tile_rect)


            #use this method to see the block on the screen





