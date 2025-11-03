#RC, 1st, Ryan Crop

#Impot libraries
import turtle
import random

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
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pendown()
    selection = True
    row = []
    col = []



    while selection == True:
        for x in col_grid:
            #For x
            y = -350
            for x in row_grid:
                m = 0
                num = random.randint(1,2)
                if num == 1:
                    pen.penup()
                    pen.goto(row_grid[m],y)
                    pen.pendown()
                    pen.forward(100)
                else:
                    pen.penup()
                    pen.goto(row_grid[m],y)
                    pen.forward(100)
                m +=1
            y += 100
        for y in row_grid:
            #For x
            x = -350
            for y in col_grid:
                m = 0
                num = random.randint(1,2)
                if num == 1:
                    pen.penup()
                    pen.goto(col_grid[m],y)
                    pen.pendown()
                    pen.forward(100)
                else:
                    pen.penup()
                    pen.goto(col_grid[m],y)
                    pen.forward(100)
                m +=1
            x += 100

        selection = False




def solvable(row_grid, col_grid):

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


walls()

turtle.done()