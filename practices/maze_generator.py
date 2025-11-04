#RC, 1st, Ryan Crop

#Impot libraries
import turtle
import random

confused = True
#set up maze screen

#Goes from -350 to -50 to 50 to 350
#Cell size should be 100
wn = turtle.Screen()
wn.bgcolor("cyan")
wn.setup(800,800)
def walls():
    wall_drawer = turtle.Turtle()
    wall_drawer.color("black")
    wall_drawer.hideturtle()
    wall_drawer.penup()
    wall_drawer.goto(350,350)
    wall_drawer.pendown()
    wall_drawer.goto(350,-350)
    wall_drawer.goto(50,-350)
    wall_drawer.penup()
    wall_drawer.goto(-50,-350)
    wall_drawer.pendown()
    wall_drawer.goto(-350,-350)
    wall_drawer.goto(-350,350)
    wall_drawer.goto(-50,350)
    wall_drawer.penup()
    wall_drawer.goto(50,350)
    wall_drawer.pendown()
    wall_drawer.goto(350,350)

row_grid = [-350,-250,-150,-50,50,150,250]
col_grid = [-350,-250,-150,-50,50,150,250]

def grid_setup(row_grid, col_grid):
    true = 0
    pen = turtle.Turtle()

    pen.pendown()
    pen.speed(10)
    selection = True
    row = []
    col = []
    y = -250


    for x in range (1,7):
        m = -350
        true = 0
        selection = True
        while selection == True:
            num = random.randint(1,2)
            if num == 1:
                pen.penup()
                pen.goto(m,y)
                pen.pendown()
                pen.forward(100)
            else:
                pen.penup()
                pen.goto(m,y)
                pen.forward(100)
            m += 100
            true += 1
            if true == 7:
                selection = False
        y += 100
    m = -250
    for x in range (1,7):
        y = -350
        true = 0
        selection = True
        while selection == True:
            num = random.randint(1,2)
            if num == 1:
                pen.penup()
                pen.goto(m,y)
                pen.pendown()
                pen.left(90)
                pen.forward(100)
            else:
                pen.penup()
                pen.goto(m,y)
                pen.left(90)
                pen.forward(100)
            y += 100
            true += 1
            pen.right(90)
            if true == 7:
                selection = False
        m += 100



def solvable(row_grid, col_grid):
    row_grid = [-350,-250,-150,-50,50,150,250]
    col_grid = [-350,-250,-150,-50,50,150,250]
    size = len(row_grid) - 1
    visited = set()
    stack = [(0,0)]

    while stack:
        x, y = stack.pop()
        if x == size -1 and y == size -1:
            return True
        
        if (x,y) in visited:
            continue

        visited.add((x,y))

        if x < size -1 and col_grid[y][x+1] == 0:
            stack.append((x+1,y))

        if y < size -1 and row_grid[y+1][x] == 0:
            stack.append((x,y+1))

        if x > 0 and col_grid[y][x] == 0:
            stack.append((x-1, y))

        if y > 0 and row_grid[y][x] == 0:
            stack.append((x,y-1))

    return False



while confused == True:
    walls()
    grid_setup("","")
    tf = solvable("","") #Figure out whats freaking out about the solvable function
    if tf == True:
        walls()
        grid_setup("","")
        confused == False
    else:
        pass

turtle.done()