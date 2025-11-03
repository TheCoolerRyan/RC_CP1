#RC, 1st, Ryan Crop

#Impot libraries
import turtle
import random

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
    spotx = [-40,-30,-20,-10,0,10,20,30,40]
    spoty = [-40,-30,-20,-10,0,10,20,30,40]
    for y in spoty:
        rany = random.randint(1,2)
        if rany == 1:
            xy = -40
            pen.penup()
            pen.sety(spoty[y])
            pen.setx(xy)
            pen.pendown()
            pen.forward(10)
            xy += 10
        else:
            xy += 10
            pass
        for x in spotx: #Create program for x
            ranx = random.randint(1,2)
            if ranx == 1:
                pen.penup()
                pen.setx(spotx[x])
                pen.sety(spoty[y])
                pen.pendown()
                pen.left(90)
                pen.forward(10)
            else:
                pass

print(posibilite("","","",""))
        #Figure out how to make it so theres always a way to win

