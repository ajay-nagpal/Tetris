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