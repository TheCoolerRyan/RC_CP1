#RC, 1st, Ryan Crop
import turtle
import random
#Figure out maze widths and height
cell_width = 10
cell_height = 10

#set up maze screen
maze = turtle.Screen()
maze.setup(100,100)
maze.tracer(0)

pen = turtle.Turtle()
pen.speed(50)
pen.hideturtle()
pen.penup()
pen.goto(0,40)
pen.pendown()
pen.goto(-40,40)
pen.goto(-40,-40)
pen.goto(0,-40)
pen.penup()
pen.goto(10,-40)
pen.pendown()
pen.goto(40,-40)
pen.goto(40,40)
pen.goto(10,40)
#Will be in a list that decides wether or not 
def posibilite(x,y,spotx,spoty):
    spotx = [-30,-20,-10,0,10,20,30]
    spoty = [-30,-20,-10,0,10,20,30]
    for y in spoty:
        rany = random.randint(1,2)
        if rany == 1:
            pen.penup()
            pen.sety(spoty[y])
            pen.pendown()
            pen.forward(10)
        else:
            pass
        for x in spotx: #Create program for x
            random.randint(1,2)
        
    #Create thing that decieds wether or not to put a white spot or a line

    #Create list

        #Figure out how to make it so theres always a way to win
        #Create start and stop spots

