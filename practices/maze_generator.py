#RC, 1st, Ryan Crop

#Impot libraries
import turtle
import random

#Set variables
confused = True

#Set up the window
wn = turtle.Screen()
wn.setup(800,800)

#Draw the border of the maze
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

#Create lists for the x axis
row_grid = [-350,-250,-150,50,150,250]
col_grid = [-350,-250,-150,50,150,250]

#Function to randomly set up the maze
def grid_setup(row, col):
    true = 0
    #Create turtle to draw the maze inside walls
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pendown()
    pen.speed(0)
    selection = True
    #Set empty lists to add cordinate values
    row = []
    col = []
    #Set starting y value
    y = -250


    for x in range (1,7):
        #Set basic x value and other values
        m = -350
        true = 0
        selection = True
        #Create while loop to go through the x axis
        while selection == True:
            #Set random number
            num = random.randint(1,3)

            #Check to see where it will end up
            if m == -50 and y == -250:
                num = 2
            if m == -50 and y == 250:
                num = 2
            if num == 1:
                #Drawing function for walls one at a time
                row.append((m,y))
                pen.penup()
                pen.goto(m,y)
                pen.pendown()
                pen.forward(100)
            else:
                #Just move forward without drawing
                pen.penup()
                pen.goto(m,y)
                pen.forward(100)
            #Increase x value and turn counter
            m += 100
            true += 1
            if true == 7:
                #end it
                selection = False
        #Add y values
        y += 100
    #set x values
    m = -250
    #Create loop to draw the lines
    for x in range (1,7):
        #Reset values for the loop
        y = -350
        true = 0
        selection = True
        #start the drawing loop
        while selection == True:
            num = random.randint(1,3)
            #Set values to check for the drawing again
            if x == -50:
                continue
            if num == 1:
                #Draw the first line with the x and why axis
                col.append((m,y))
                pen.penup()
                pen.goto(m,y)
                pen.pendown()
                pen.left(90)
                pen.forward(100)
            else:
                #Go to the same places without drawing
                pen.penup()
                pen.goto(m,y)
                pen.left(90)
                pen.forward(100)
            #Increase the values and reset the turtle angle
            y += 100
            true += 1
            pen.right(90)
            #Conditional to end the loop
            if true == 7:
                selection = False
        #Increase x
        m += 100
    #Return values
    return row, col


#Create function to check if its solvable
def solvable(col , row):
    #set up the basic variables
    size = len(row) - 1
    visited = set()
    stack = [(0,0)]

    #Create loop for checking
    while stack:
        #Get rid of excese x/y values
        x, y = stack.pop()
        #Check to see if were at the end
        if x == size-1  and y == size-1 :
            return True
        #See if you have already been there
        if (x,y) in visited:
            continue
        #Add the value to visited
        visited.add((x,y))
        #Check to see if we can go right
        if x < size -1 and col[y][x+1] == 0:
            stack.append((x+1,y))
        #Check to see if we can go up
        if y < size -1 and row[y+1][x] == 0:
            stack.append((x,y+1))
        #Check to see if we can go to the left
        if x > 0 and col[y][x] == 0:
            stack.append((x-1, y))
        #Check to see if we can go down
        if y > 0 and row[y][x] == 0:
            stack.append((x,y-1))
        #Excese checking values
        num = random.randint(1,2)
        if num == 1:
            return True
        else:
            pass
    #Return values
    return False


#Loop to keep the functions going
while confused == True:
    #Stop the updates
    wn.tracer(0)
    walls()
    #Go through the generations and the solvable
    row, col = grid_setup("","")
    if solvable(col,row) == True: #Figure out whats freaking out about the solvable function
        #Update screen and exit loop
        wn.update()
        confused = False
    else:
        #Get rid of drawings and continue
        turtle.clearscreen()
        pass
#Make it so it doesn't dissapear
turtle.done()