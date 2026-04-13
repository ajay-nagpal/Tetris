from block import Block
from position import Position


class LBlock(Block):
    """
    ___| rotation state:0, cells occupied[(1,0)  (1,1)  (1,2)  (0,2)]
    
    """
    def __init__(self):
        super().__init__(id=1)
        #now we need to declare which cell are occupied
        # we will use cell of block class
        # this is going to be  dict
        #key will be rotation state(0 to 3)
        #value wil; be list , contiaing value of occupied cells
        self.cells={
            0:[Position(0,2),Position(1,0),Position(1,1),Position(1,2)],
            1:[Position(0,1),Position(1,1),Position(2,1),Position(2,2)],#L
            2:[Position(1,0),Position(1,1),Position(1,2),Position(2,0)],
            3:[Position(0,0),Position(0,1),Position(1,1),Position(2,1)]
        }

        #currently each block origin is top left (0,0)
        #we need it to start from top middle
        #initially move it to 4 cells to make it appear from middle
        self.move(0,4)


class JBlock(Block):
    
    def __init__(self):
        super().__init__(id=2)
        #now we need to declare which cell are occupied
        # we will use cell of block class
        # this is going to be  dict
        #key will be rotation state(0 to 3)
        #value wil; be list , contiaing value of occupied cells
        self.cells={
            0:[Position(0,0),Position(1,0),Position(1,1),Position(1,2)],
            1:[Position(0,1),Position(0,2),Position(1,1),Position(2,1)],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(2,2)],
            3:[Position(0,1),Position(1,1),Position(2,0),Position(2,1)]
        }
        self.move(0,4)


class IBlock(Block):
    
    def __init__(self):
        super().__init__(id=3)
        #now we need to declare which cell are occupied
        # we will use cell of block class
        # this is going to be  dict
        #key will be rotation state(0 to 3)
        #value wil; be list , contiaing value of occupied cells
        self.cells={
            0:[Position(1,0),Position(1,1),Position(1,2),Position(1,3)],
            1:[Position(0,2),Position(1,2),Position(2,2),Position(3,2)],
            2:[Position(2,0),Position(2,1),Position(2,2),Position(2,3)],
            3:[Position(0,1),Position(1,1),Position(2,1),Position(3,1)]
        }
        self.move(-1,4)#-1 becasue , ther will be one empty row on top at beginnign of this block


class OBlock(Block):
    
    def __init__(self):
        super().__init__(id=4)
        #now we need to declare which cell are occupied
        # we will use cell of block class
        # this is going to be  dict
        #key will be rotation state(0 to 3)
        #value wil; be list , contiaing value of occupied cells
        self.cells={
            0:[Position(0,0),Position(0,1),Position(1,0),Position(1,1)],
            1:[Position(0,0),Position(0,1),Position(1,0),Position(1,1)],
            2:[Position(0,0),Position(0,1),Position(1,0),Position(1,1)],
            3:[Position(0,0),Position(0,1),Position(1,0),Position(1,1)]
        }
        self.move(0,5)


class SBlock(Block):
    
    def __init__(self):
        super().__init__(id=5)
        #now we need to declare which cell are occupied
        # we will use cell of block class
        # this is going to be  dict
        #key will be rotation state(0 to 3)
        #value wil; be list , contiaing value of occupied cells
        self.cells={
            0:[Position(0,1),Position(0,2),Position(1,0),Position(1,1)],
            1:[Position(0,1),Position(1,1),Position(1,2),Position(2,2)],
            2:[Position(1,1),Position(1,2),Position(2,0),Position(2,1)],
            3:[Position(0,0),Position(1,0),Position(1,1),Position(2,1)]
        }
        self.move(0,4)


class TBlock(Block):
    
    def __init__(self):
        super().__init__(id=6)
        #now we need to declare which cell are occupied
        # we will use cell of block class
        # this is going to be  dict
        #key will be rotation state(0 to 3)
        #value wil; be list , contiaing value of occupied cells
        self.cells={
            0:[Position(0,1),Position(1,0),Position(1,1),Position(1,2)],
            1:[Position(0,1),Position(1,1),Position(1,2),Position(2,1)],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(2,1)],
            3:[Position(0,1),Position(1,0),Position(1,1),Position(2,1)]
        }
        self.move(0,4)


class ZBlock(Block):
    
    def __init__(self):
        super().__init__(id=7)
        #now we need to declare which cell are occupied
        # we will use cell of block class
        # this is going to be  dict
        #key will be rotation state(0 to 3)
        #value wil; be list , contiaing value of occupied cells
        self.cells={
            0:[Position(0,0),Position(0,1),Position(1,1),Position(1,2)],
            1:[Position(0,2),Position(1,1),Position(1,2),Position(2,1)],
            2:[Position(1,0),Position(1,1),Position(2,1),Position(2,2)],
            3:[Position(0,1),Position(1,0),Position(1,1),Position(2,0)]
        }
        self.move(0,4)



