'''
name: Saki Imai
file: tetris.py
course: CS151 C2 fall
description: This is a program for the game tetris.
'''


import turtle
import time 
import random


class Shape:
    def __init__(self):
        '''initizlizes a shape'''

        self.row = 0
        self.col = 3
        self.color = random.randint(1, 7)
        self.shape = []


    def get_row(self):
        ''' returns the row number of the block'''
        return self.row
    

    def get_col(self):
        ''' returns the column number of the block'''
        return self.col
    

    def get_color(self):
        ''' returns the color of the block'''
        return self.color
    

    def get_shape(self):
        ''' returns the shape of the block'''
        return self.shape


    def set_row(self, new_row):
        '''sets the new row number of the block'''
        self.row = new_row


    def set_col(self, new_col):
        '''sets the new column number of the block'''
        self.col = new_col
    

    def move_down(self):
        ''' moves the block down by 1 '''

        self.row += 1
        for index in range(len(self.shape)):
            row = self.shape[index][0]
            self.shape[index] = (row + 1, self.shape[index][1])


    def move_left(self):
        ''' moves the block left by 1'''

        self.col -= 1
        for index in range(len(self.shape)):
            col = self.shape[index][1]
            self.shape[index] = (self.shape[index][0], col - 1)


    def move_right(self):
        ''' moves the block right by 1'''
        
        self.col += 1
        for index in range(len(self.shape)):
            col = self.shape[index][1]
            self.shape[index] = (self.shape[index][0], col + 1)
    

class S_Shape(Shape):
    def __init__(self):
        '''initizlizes a S shape'''

        Shape.__init__(self)
        self.shape = [(self.row, self.col+1), (self.row, self.col+2),(self.row + 1, self.col), (self.row + 1, self.col + 1)]


    def rotate_right(self):
        '''rotate the tetromino to the right'''

        if self.shape == [(self.row, self.col+1), (self.row, self.col+2),(self.row + 1, self.col), (self.row + 1, self.col + 1)]:
            self.shape = [(self.row, self.col+1), (self.row + 1, self.col+1), (self.row + 1, self.col + 2), (self.row + 2, self.col + 2)]
        elif self.shape == [(self.row, self.col+1), (self.row + 1, self.col+1), (self.row + 1, self.col + 2), (self.row + 2, self.col + 2)]:
            self.shape = [(self.row, self.col+1), (self.row, self.col+2),(self.row + 1, self.col), (self.row + 1, self.col + 1)]


    def rotate_left(self):
        '''rotate the tetromino to the left'''

        if self.shape == [(self.row, self.col+1), (self.row, self.col+2),(self.row + 1, self.col), (self.row + 1, self.col + 1)]:
            self.shape = [(self.row, self.col+1), (self.row+1, self.col+1),(self.row + 1, self.col+2), (self.row + 2, self.col + 2)]
        elif self.shape == [(self.row, self.col+1), (self.row+1, self.col+1),(self.row + 1, self.col+2), (self.row + 2, self.col + 2)]:
            self.shape = [(self.row, self.col+1), (self.row, self.col+2),(self.row + 1, self.col), (self.row + 1, self.col + 1)]


class Z_Shape(Shape):
    def __init__(self):
        '''initizlizes a Z shape'''

        Shape.__init__(self)
        self.shape = [(self.row, self.col), (self.row, self.col+1), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]


    def rotate_right(self):
        '''rotate the tetromino to the right'''

        if self.shape == [(self.row, self.col), (self.row, self.col+1), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]:
            self.shape = [(self.row, self.col+1), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 2, self.col)]
        elif self.shape == [(self.row, self.col+1), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 2, self.col)]:
            self.shape = [(self.row, self.col), (self.row, self.col+1), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]


    def rotate_left(self):
        '''rotate the tetromino to the left'''

        if self.shape == [(self.row, self.col), (self.row, self.col+1), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]:
            self.shape = [(self.row, self.col+1), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 2, self.col)]
        elif self.shape == [(self.row, self.col+1), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 2, self.col)]:
            self.shape = [(self.row, self.col), (self.row, self.col+1), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]


class T_Shape(Shape):
    def __init__(self):
        '''initizlizes a T shape'''

        Shape.__init__(self)
        self.shape = [(self.row, self.col+1), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]


    def rotate_right(self):
        '''rotate the tetromino to the right'''

        if self.shape == [(self.row, self.col+1), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]:
            self.shape = [(self.row, self.col+1), (self.row + 1, self.col+1), (self.row + 1, self.col + 2), (self.row + 2, self.col + 1)]
        elif self.shape == [(self.row, self.col+1), (self.row + 1, self.col+1), (self.row + 1, self.col + 2), (self.row + 2, self.col + 1)]:
            self.shape = [(self.row, self.col), (self.row, self.col + 1), (self.row, self.col + 2), (self.row + 1, self.col + 1)]
        elif self.shape == [(self.row, self.col), (self.row, self.col + 1), (self.row, self.col + 2), (self.row + 1, self.col + 1)]:
            self.shape = [(self.row, self.col+1), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 2, self.col + 1)]
        elif self.shape == [(self.row, self.col+1), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 2, self.col + 1)]:
            self.shape = [(self.row, self.col+1), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]


    def rotate_left(self):
        '''rotate the tetromino to the left'''

        if self.shape == [(self.row, self.col+1), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]:
            self.shape = [(self.row, self.col+1), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 2, self.col + 1)]
        elif self.shape == [(self.row, self.col+1), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 2, self.col + 1)]:
            self.shape = [(self.row, self.col), (self.row, self.col + 1), (self.row, self.col + 2), (self.row + 1, self.col + 1)]
        elif self.shape == [(self.row, self.col), (self.row, self.col + 1), (self.row, self.col + 2), (self.row + 1, self.col + 1)]:
            self.shape = [(self.row, self.col+1), (self.row + 1, self.col+1), (self.row + 1, self.col + 2), (self.row + 2, self.col + 1)]
        elif self.shape == [(self.row, self.col+1), (self.row + 1, self.col+1), (self.row + 1, self.col + 2), (self.row + 2, self.col + 1)]:
            self.shape = [(self.row, self.col+1), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]


class L_Shape(Shape):
    def __init__(self):
        '''initizlizes a L shape'''

        Shape.__init__(self)
        self.shape = [(self.row, self.col), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]
    

    def rotate_right(self):
        '''rotate the tetromino to the right'''

        if self.shape == [(self.row, self.col), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]:
            self.shape = [(self.row, self.col), (self.row, self.col + 1), (self.row + 1, self.col), (self.row + 2, self.col)]
        elif self.shape == [(self.row, self.col), (self.row, self.col + 1), (self.row + 1, self.col), (self.row + 2, self.col)]:
            self.shape = [(self.row, self.col), (self.row, self.col + 1), (self.row, self.col + 2), (self.row + 1, self.col + 2)]
        elif self.shape == [(self.row, self.col), (self.row, self.col + 1), (self.row, self.col + 2), (self.row + 1, self.col + 2)]:
            self.shape = [(self.row, self.col+2), (self.row + 1, self.col + 2), (self.row + 2, self.col + 1), (self.row + 2, self.col + 2)]
        elif self.shape == [(self.row, self.col+2), (self.row + 1, self.col + 2), (self.row + 2, self.col + 1), (self.row + 2, self.col + 2)]:
            self.shape = [(self.row, self.col), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]
    

    def rotate_left(self):
        '''rotate the tetromino to the left'''

        if self.shape == [(self.row, self.col), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]:
            self.shape = [(self.row, self.col+2), (self.row + 1, self.col + 2), (self.row + 2, self.col + 1), (self.row + 2, self.col + 2)]
        elif self.shape == [(self.row, self.col+2), (self.row + 1, self.col + 2), (self.row + 2, self.col + 1), (self.row + 2, self.col + 2)]:
            self.shape = [(self.row, self.col), (self.row, self.col + 1), (self.row, self.col + 2), (self.row + 1, self.col + 2)]
        elif self.shape == [(self.row, self.col), (self.row, self.col + 1), (self.row, self.col + 2), (self.row + 1, self.col + 2)]:
            self.shape = [(self.row, self.col), (self.row, self.col + 1), (self.row + 1, self.col), (self.row + 2, self.col)]
        elif self.shape == [(self.row, self.col), (self.row, self.col + 1), (self.row + 1, self.col), (self.row + 2, self.col)]:
            self.shape = [(self.row, self.col), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]


class I_Shape(Shape):
    def __init__(self):
        '''initizlizes an I shape'''

        Shape.__init__(self)
        self.shape = [(self.row, self.col), (self.row, self.col+1), (self.row, self.col+2), (self.row, self.col+3)]


    def rotate_right(self):
        '''rotate the tetromino to the right'''

        if self.shape == [(self.row, self.col), (self.row, self.col+1), (self.row, self.col+2), (self.row, self.col+3)]:
            self.shape = [(self.row -1, self.col), (self.row, self.col), (self.row + 1, self.col), (self.row + 2, self.col)]
        elif self.shape == [(self.row -1, self.col), (self.row, self.col), (self.row + 1, self.col), (self.row + 2, self.col)]:
            self.shape = [(self.row, self.col), (self.row, self.col+1), (self.row, self.col+2), (self.row, self.col+3)]


    def rotate_left(self):
        '''rotate the tetromino to the left'''

        if self.shape == [(self.row, self.col), (self.row, self.col+1), (self.row, self.col+2), (self.row, self.col+3)]:
            self.shape = [(self.row -1, self.col), (self.row, self.col), (self.row + 1, self.col), (self.row + 2, self.col)]
        elif self.shape == [(self.row -1, self.col), (self.row, self.col), (self.row + 1, self.col), (self.row + 2, self.col)]:
            self.shape = [(self.row, self.col), (self.row, self.col+1), (self.row, self.col+2), (self.row, self.col+3)]
    

class J_Shape(Shape):
    def __init__(self):
        '''initizlizes a J shape'''

        Shape.__init__(self)
        self.shape = [(self.row, self.col+2), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]


    def rotate_right(self):
        '''rotate the tetromino to the right'''

        if self.shape == [(self.row, self.col+2), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]:
            self.shape = [(self.row, self.col + 1), (self.row + 1, self.col + 1), (self.row + 2, self.col + 1), (self.row + 2, self.col + 2)]
        elif self.shape == [(self.row, self.col + 1), (self.row + 1, self.col + 1), (self.row + 2, self.col + 1), (self.row + 2, self.col + 2)]:
            self.shape = [(self.row, self.col), (self.row, self.col + 1), (self.row, self.col + 2), (self.row + 1, self.col)]
        elif self.shape == [(self.row, self.col), (self.row, self.col + 1), (self.row, self.col + 2), (self.row + 1, self.col)]:
            self.shape = [(self.row, self.col), (self.row, self.col + 1), (self.row + 1, self.col + 1), (self.row + 2, self.col + 1)]
        elif self.shape == [(self.row, self.col), (self.row, self.col + 1), (self.row + 1, self.col + 1), (self.row + 2, self.col + 1)]:
            self.shape = [(self.row, self.col+2), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]


    def rotate_left(self):
        '''rotate the tetromino to the left'''

        if self.shape == [(self.row, self.col+2), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]:
            self.shape = [(self.row, self.col+1), (self.row, self.col+2), (self.row + 1, self.col + 2), (self.row + 2, self.col + 2)]
        elif self.shape == [(self.row, self.col+1), (self.row, self.col+2), (self.row + 1, self.col + 2), (self.row + 2, self.col + 2)]:
            self.shape = [(self.row, self.col+2), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]
        elif self.shape == [(self.row, self.col+2), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]:
            self.shape = [(self.row, self.col + 1), (self.row + 1, self.col + 1), (self.row + 2, self.col + 1), (self.row + 2, self.col + 2)]
        elif self.shape == [(self.row, self.col + 1), (self.row + 1, self.col + 1), (self.row + 2, self.col + 1), (self.row + 2, self.col + 2)]:
            self.shape = [(self.row, self.col+2), (self.row + 1, self.col), (self.row + 1, self.col + 1), (self.row + 1, self.col + 2)]


class O_Shape(Shape):
    def __init__(self):
        '''initizlizes an O shape'''

        Shape.__init__(self)
        self.shape = [(self.row, self.col), (self.row, self.col+1), (self.row + 1, self.col), (self.row + 1, self.col + 1)]


    def rotate_right(self):
        '''rotate the tetromino to the right'''
        return


    def rotate_left(self):
        '''rotate the tetromino to the left'''
        return


class Game:
    def __init__(self):
        self.turt = turtle.Turtle()
        self.turt.shape('square')
        self.turt.color('black')
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.tilesize = 20
        self.x_offset = -35
        self.y_offset = 215

        #setting up score writing turtle
        self.score_turt = turtle.Turtle()
        self.score_turt.hideturtle()
        self.score_turt.up()
        self.score_turt.goto(-150, -120)
        self.score_turt.down()
        self.score = 0
        self.score_turt.write("Score:" + str(self.score), font = ('Arial', 20, 'normal'))

        #setting up writing turtle
        self.writing_turt = turtle.Turtle()
        self.writing_turt.hideturtle()
        self.writing_turt.color('white')

        #generating a tetromino
        shape_index = random.randint(0, 6)
        if shape_index == 0:
            self.shape = S_Shape()
        elif shape_index == 1:
            self.shape = Z_Shape()
        elif shape_index == 2:
            self.shape = T_Shape()
        elif shape_index == 3:
            self.shape = L_Shape()
        elif shape_index == 4:
            self.shape = I_Shape()
        elif shape_index == 5:
            self.shape = J_Shape()
        elif shape_index == 6:
            self.shape = O_Shape()
    

    def draw(self):
        ''' draws the game scene '''

        self.turt.clear()
        
        #prints out the grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                self.turt.up()
                self.turt.goto(col * self.tilesize + self.x_offset, -row * self.tilesize + self.y_offset)
                self.turt.down()

                if self.grid[row][col] == 0:
                    self.turt.color("black")
                    self.turt.stamp()
                elif self.grid[row][col] == 1:
                    self.turt.color("cyan")
                    self.turt.stamp()
                elif self.grid[row][col] == 2:
                    self.turt.color("red")
                    self.turt.stamp()
                elif self.grid[row][col] == 3:
                    self.turt.color("orange")
                    self.turt.stamp()
                elif self.grid[row][col] == 4:
                    self.turt.color("blue")
                    self.turt.stamp()
                elif self.grid[row][col] == 5:
                    self.turt.color("green")
                    self.turt.stamp()
                elif self.grid[row][col] == 6:
                    self.turt.color("purple")
                    self.turt.stamp()
                elif self.grid[row][col] == 7:
                    self.turt.color("yellow")
                    self.turt.stamp()

        #prints out the moving block
        for row,col in self.shape.get_shape():
            self.turt.up()
            self.turt.goto(col * self.tilesize + self.x_offset, -row * self.tilesize + self.y_offset)
            self.turt.down()
            if self.shape.get_color() == 1:
                self.turt.color("cyan")
            elif self.shape.get_color() == 2:
                self.turt.color("red")
            elif self.shape.get_color() == 3:
                self.turt.color("orange")
            elif self.shape.get_color() == 4:
                self.turt.color("blue")
            elif self.shape.get_color() == 5:
                self.turt.color("green")
            elif self.shape.get_color() == 6:
                self.turt.color("purple")
            elif self.shape.get_color() == 7:
                self.turt.color("yellow")
            self.turt.stamp()
            

    def move_down(self):
        ''' move the block down by 1 '''
        
        # checking over all the blocks 
        can_move = True
        for row,col in self.shape.get_shape():
            # check if the block is within the grid and if there is a block right below 
            if self.shape.shape[-1][0] >= 21 or self.grid[row + 1][col] != 0: 
                can_move = False

        #if the block is not allowed to move down
        if can_move == False:
            for row,col in self.shape.get_shape():
                self.grid[row][col] = self.shape.get_color()

                #check if the grid is filled with blocks
                if self.shape.get_shape()[0][0] == 0:
                     self.game_over()
                     return

            #create a new shape
            shape_index = random.randint(0, 6)
            if shape_index == 0:
                self.shape = S_Shape()
            elif shape_index == 1:
                self.shape = Z_Shape()
            elif shape_index == 2:
                self.shape = T_Shape()
            elif shape_index == 3:
                self.shape = L_Shape()
            elif shape_index == 4:
                self.shape = I_Shape()
            elif shape_index == 5:
                self.shape = J_Shape()
            elif shape_index == 6:
                self.shape = O_Shape()

        #if the block is allowed to move down
        else:
            self.shape.move_down()

    
    def move_left(self):
        ''' calls the shape.move_left function if the block is allowed to move left'''

        if self.shape.get_col() > 0:
            self.shape.move_left()


    def move_right(self):
        ''' calls the shape.move_right function if the block is allowed to move right'''

        for index in range(len(self.shape.get_shape())):
            if self.shape.get_shape()[index][1] >= 9:
                return
        self.shape.move_right()
    

    def game_over(self):
        '''starts the game all over again'''

        global start_time
        self.writing_turt.up()
        self.writing_turt.goto(-20, 50)
        self.writing_turt.down()
        self.writing_turt.write("GAME OVER", font = ('Arial', 25, 'normal'))
        time.sleep(1)
        self.writing_turt.clear()
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        #generating new tetromino
        shape_index = random.randint(0, 6)
        if shape_index == 0:
            self.shape = S_Shape()
        elif shape_index == 1:
            self.shape = Z_Shape()
        elif shape_index == 2:
            self.shape = T_Shape()
        elif shape_index == 3:
            self.shape = L_Shape()
        elif shape_index == 4:
            self.shape = I_Shape()
        elif shape_index == 5:
            self.shape = J_Shape()
        elif shape_index == 6:
            self.shape = O_Shape()

        #resetting the score
        self.score = 0
        self.score_turt.clear()
        self.score_turt.write("Score:" + str(self.score), font = ('Arial', 20, 'normal'))
        self.writing_turt.up()
        self.writing_turt.goto(50, 50)
        self.writing_turt.down()

        #counting down until the next game starts
        for i in range(3):
            self.writing_turt.clear()
            self.writing_turt.write(3-i, font = ('Arial', 25, 'normal'))
            time.sleep(1)
        start_time = time.time()
    

    def clear(self):
        '''go over all the rows and columns in the grid and delete the row filled with tetrominos'''

        #check if there are rows filled with blocks
        for row in range(21, 0, -1):
            can_clear = True
            for col in range(0, 10):
                if self.grid[row][col] == 0:
                    can_clear = False
                    continue

            # if the row is filled with blocks
            if can_clear == True:
                #copy the information of the cell right above each cell
                if row == 21:
                    for col2 in range(0, 10):
                        self.grid[row][col2] = self.grid[row-1][col2]
                else:
                    for col2 in range(0, 10):
                        self.grid[row][col2] = self.grid[row-1][col2]
                for row2 in range(row-1, 0, -1):
                    for col2 in range(0, 10):
                        self.grid[row2][col2] = self.grid[row2-1][col2]

                #inserting a new row that replaces the deleted row
                for row2 in range(0, 1):
                    for col2 in range(0, 10):
                        self.grid[row2][col2] = 0

                #increase and rewrite the score on the screen
                self.score += 100
                self.score_turt.clear()
                self.score_turt.write("Score:" + str(self.score), font = ('Arial', 20, 'normal'))


    def rotate_right(self):
        '''rotate the tetromino to the right '''
        self.shape.rotate_right()
    

    def rotate_left(self):
        '''rotate the tetromino to the left '''
        self.shape.rotate_left()


#setting up start_time in global scope
start_time = time.time()


def main():
    '''this is my main funtion'''

    #setting up window
    window = turtle.getscreen()
    window.bgcolor('white')
    window.title("Tetris")
    window.setup(350, 470)
    window.tracer(0)

    #setting up turtle
    turt = turtle.Turtle()
    turt.up()
    turt.goto(-150, 180)
    turt.down()
    turt.color("red")
    turt.hideturtle()
    turt.write("TETRIS", font = ('Arial', 25, 'normal'))
    turt.hideturtle()

    #setting up time writing turtle
    time_writer = turtle.Turtle()
    time_writer.up()
    time_writer.goto(-150, -160)
    time_writer.color("black")
    time_writer.write("Time: ", font = ('Arial', 20, 'normal'))
    time_writer.hideturtle()

    my_game = Game()
    my_game.draw()

    #keyboard bindings
    window.listen()
    window.onkeypress(my_game.move_left, "Left")
    window.onkeypress(my_game.move_right, "Right")
    window.onkeypress(my_game.rotate_right, "w")
    window.onkeypress(my_game.rotate_left, "s")

    #main while loop
    while True:
        window.update()
        time.sleep(0.1)
        current_time = time.time()
        play_time = int(current_time - start_time)
        time_writer.clear()
        time_writer.write("Time: " + str(play_time), font = ('Arial', 20, 'normal'))
        my_game.move_down()
        my_game.clear()
        my_game.draw()
    
main()
