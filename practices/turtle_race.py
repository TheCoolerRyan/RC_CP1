#RC, 1st, turtle race
import turtle
import random

wn = turtle.Screen()
wn.title("My Turtle Graphics")
wn.bgcolor("lightblue")


f_line = turtle.Turtle()
f_line.hideturtle()
f_line.color("black")
f_line.penup()
f_line.setx(500)
f_line.sety(-550)
f_line.pendown()
f_line.pensize(3)
f_line.goto(500,550)
f_line.forward(150)
f_line.right(90)
f_line.forward(1100)
f_line.right(90)
f_line.forward(150)
f_line.setx(500)
f_line.sety(550)


writing = turtle.Turtle()
writing.hideturtle()
writing.penup()
writing.goto(500,500)
writing.pendown()
writing.pencolor("black")
writing.pensize(2)


def turtles(black, green, red, yellow, orange, purple):
    game = True
    wn.tracer(0)
    black = turtle.Turtle()
    black.shape("turtle")
    black.color("black")
    black.penup()
    black.goto(0,500)
    black.pendown()

    green = turtle.Turtle()
    green.shape("turtle")
    green.color("green")
    green.penup()
    green.goto(0,300)
    green.pendown()

    red = turtle.Turtle()
    red.shape("turtle")
    red.color("red")
    red.penup()
    red.goto(0,100)
    red.pendown()

    yellow = turtle.Turtle()
    yellow.shape("turtle")
    yellow.color("yellow")
    yellow.penup()
    yellow.goto(0,-100)
    yellow.pendown()

    orange = turtle.Turtle()
    orange.shape("turtle")
    orange.color("orange")
    orange.penup()
    orange.goto(0,-300)
    orange.pendown()

    purple = turtle.Turtle()
    purple.shape("turtle")
    purple.color("purple")
    purple.penup()
    purple.goto(0,-500)
    purple.pendown()

    wn.update()
    wn.tracer(1)
    #Make turtle move
    while game == True:
        black.forward(random.randint(1,10))
        if black.xcor() > 499:
            game = False
            print("Black Wins!",font =( "Arial", 51, "bold"))
        green.forward(random.randint(1,10))
        if green.xcor() > 499:
            game = False
            print("Green Wins!",font =( "Arial", 51, "bold"))
        red.forward(random.randint(1,10))
        if red.xcor() > 499:
            game = False
            print("Red Wins!",font =( "Arial", 51, "bold"))
        yellow.forward(random.randint(1,10))
        if yellow.xcor() > 499:
            game = False
            print("Yellow Wins!",font =( "Arial", 51, "bold"))
        orange.forward(random.randint(1,10))
        if orange.xcor() > 499:
            game = False
            print("Orange Wins!",font =( "Arial", 51, "bold"))
        purple.forward(random.randint(1,10))
        if purple.xcor() > 499:
            game = False
            print("Purple Wins!",font =( "Arial", 51, "bold"))
    return black, green, red, yellow, orange, purple

#Figure out how to make turtles move at the same time.
turtles("", "", "", "", "", "")

turtle.done()
#Fix it so they dont off them selves.