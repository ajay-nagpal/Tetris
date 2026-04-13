import pygame
from color import Colors

class Grid:
    def __init__(self):
        self.rows=20
        self.cols=12
        self.cell_size=40
        self.grid=[[0 for j in range(self.cols)]for i in range(self.rows)]
        #7 block, each with unique color
        #light grey for empty
        # self.colors=self.get_cell_colors()
        self.colors=Colors.get_cell_colors()


    def print_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col],end=" ")
            print()

    def draw_grid(self,game_screen,):
        for row in range(self.rows):
            for col in range(self.cols):
                cell_value=self.grid[row][col]
                #create a rectangle cell to contain this cell imaginary , which will help us in cell filling
                cell_rect=pygame.Rect(col*self.cell_size+1,row*self.cell_size+1
                                      ,self.cell_size-1,self.cell_size-1)#need its x,y co-ord form top left corner and width and height

                #now draw
                pygame.draw.rect(game_screen,self.colors[cell_value],cell_rect)# sureface to draw on, color and rect, surface we have in tetris.p as game_screen


    def is_inside_grid(self,row,col):
        if row>=0 and row<self.rows and col>=0 and col<self.cols:
            return True
        return False
    #add a methjod in game class to cehk inside a game window

    def is_empty(self,row,col):
        if self.grid[row][col]==0:
            return True
        return False 
    
    # now we need to clear the fully occupied rows and move downall incompleted rows above it
    #first cehck if row is full
    def is_row_full(self,row):
        for col in range(self.cols):
            if self.grid[row][col]==0:
                return False
        return True
    
    # now method rto clear teh row set each cell to zero
    def clear_row(self,row):
        for col in range(self.cols):
            self.grid[row][col]=0

    #move down by specific number of rows
    def move_row_down(self,row,num_rows):
        for col in range(self.cols):
            self.grid[row+num_rows][col]=self.grid[row][col]
            #clear it
            self.grid[row][col]=0
    
    def clear_full_rows(self):
        completed=0
        #check for all rows form bottom to top if any completed , this will tell us 
        # nums rows to shift and clear
        for row in range(self.rows-1,0,-1):#19 to 0, 20 rows
            if self.is_row_full(row):
                self.clear_row(row)
                completed+=1
            elif completed>0:
                self.move_row_down(row,completed)
        return completed# to calculate the score
    
    def reset(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col]=0
            

