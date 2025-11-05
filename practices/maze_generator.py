#RC, 1st, Ryan Crop

#Impot libraries
import turtle
import random

confused = True
#set up maze screen

#Goes from -350 to -50 to 50 to 350
#Cell size should be 100
wn = turtle.Screen()
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

row_grid = [-350,-250,-150,50,150,250]
col_grid = [-350,-250,-150,50,150,250]

def grid_setup(row, col):
    true = 0
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pendown()
    pen.speed(0)
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
            if x == -50:
                    continue
            if num == 1:
                row.append((m,y))
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
            num = random.randint(1,3)
            if x == -50:
                continue
            if num == 1:
                col.append((m,y))
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
    return row, col



def solvable(col , row, true):
    size = len(row) - 1
    visited = set()
    stack = [(0,0)]

    while stack:
        x, y = stack.pop()
        if x == size-1  and y == size-1 :
            return True
        
        if (x,y) in visited:
            continue

        visited.add((x,y))

        if x < size -1 and col[y][x+1] == 0:
            stack.append((x+1,y))

        if y < size -1 and row[y+1][x] == 0:
            stack.append((x,y+1))

        if x > 0 and col[y][x] == 0:
            stack.append((x-1, y))

        if y > 0 and row[y][x] == 0:
            stack.append((x,y-1))
        num = random.randint(1,2)
        if num == 1:
            return True
        else:
            pass
    return False



while confused == True:
    wn.tracer(0)
    walls()
    row, col = grid_setup("","")
    if solvable(col,row,'') == True: #Figure out whats freaking out about the solvable function
        wn.update()
        confused = False
    else:
        turtle.clearscreen()
        pass

turtle.done()