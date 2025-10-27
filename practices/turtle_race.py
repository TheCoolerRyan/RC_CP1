#RC, 1st, turtle race
import turtle

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

def turtles(black, green, red, yellow, orange, purple):
    wn.tracer(0)
    black = turtle.Turtle()
    black.shape("turtle")
    black.color("black")
    black.penup()
    black.goto(0,500)

    green = turtle.Turtle()
    green.shape("turtle")
    green.color("green")
    green.penup()
    green.goto(0,300)

    red = turtle.Turtle()
    red.shape("turtle")
    red.color("red")
    red.penup()
    red.goto(0,100)

    yellow = turtle.Turtle()
    yellow.shape("turtle")
    yellow.color("yellow")
    yellow.penup()
    yellow.goto(0,-100)

    orange = turtle.Turtle()
    orange.shape("turtle")
    orange.color("orange")
    orange.penup()
    orange.goto(0,-300)

    purple = turtle.Turtle()
    purple.shape("turtle")
    purple.color("purple")
    purple.penup()
    purple.goto(0,-500)
    wn.update()
    return black, green, red, yellow, orange, purple

#Figure out how to make turtles move at the same time.
turtles("", "", "", "", "", "")

turtle.done()
#-1275 to 1275