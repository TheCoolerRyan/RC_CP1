#RC, 1st, turtle race

#Import librays to acsees other functions and classes
import turtle
import random

#Create screen to do stuff on
wn = turtle.Screen()
#Title screen a name
wn.title("My Turtle Graphics")
#Change color of screen because white is boring
wn.bgcolor("lightblue")

#Create finishline turtle
f_line = turtle.Turtle()
#Hide the turtle
f_line.hideturtle()
#Make the color of the turtles line black
f_line.color("black")
#Make the pen go up so it doesn't draw were its not suppolsed to
f_line.penup()
#Set turtles placement to correct x & y statements
f_line.setx(500)
f_line.sety(-550)
#Bring down turtles pen so it can draw
f_line.pendown()
#Make line thicker than usual
f_line.pensize(3)
#Give dirrections to make a big rectangular finish line
f_line.goto(500,550)
f_line.forward(150)
f_line.right(90)
f_line.forward(1100)
f_line.right(90)
f_line.forward(150)
#Reset turtles x and y to keep them out of the way
f_line.setx(500)
f_line.sety(550)

#Create turtle to help with showing the winner
writing = turtle.Turtle()
#Hide them so they don't interfer with the race
writing.hideturtle()
#Bring up pen so it doesn't draw
writing.penup()
#Set y to 500 for later print statement
writing.goto(0,500)
#Get ready to draw
writing.pendown()
#Change pencolor to black
writing.pencolor("black")
#Increase pen size for bigger efect.
writing.pensize(2)

#Create function for turtle race
def turtles(black, green, red, yellow, orange, purple):
    #set variable to True to keep the game going.
    game = True
    #Pause the updates
    wn.tracer(0)

    #Create the black turtle and its positioning
    black = turtle.Turtle()
    black.shape("turtle")
    black.color("black")
    black.penup()
    black.goto(0,500)
    black.pendown()

    #Create the green turtle and its positioning
    green = turtle.Turtle()
    green.shape("turtle")
    green.color("green")
    green.penup()
    green.goto(0,300)
    green.pendown()

    #Create the red turtle and its positioning
    red = turtle.Turtle()
    red.shape("turtle")
    red.color("red")
    red.penup()
    red.goto(0,100)
    red.pendown()

    #Create the yellow turtle and its positioning
    yellow = turtle.Turtle()
    yellow.shape("turtle")
    yellow.color("yellow")
    yellow.penup()
    yellow.goto(0,-100)
    yellow.pendown()

    #Create the orange turtle and its positioning
    orange = turtle.Turtle()
    orange.shape("turtle")
    orange.color("orange")
    orange.penup()
    orange.goto(0,-300)
    orange.pendown()

    #Create the purple turtle and its positioning
    purple = turtle.Turtle()
    purple.shape("turtle")
    purple.color("purple")
    purple.penup()
    purple.goto(0,-500)
    purple.pendown()
    #Update the window and make it constently continue to update again
    wn.update()
    wn.tracer(1)

    #Loop to keep the turtles moving until one reaches the finish line
    while game == True:
        #Create movement for turtle
        black.forward(random.randint(1,51))
        #If statement to check if they reached the finish line
        if black.xcor() > 499:
            #Print of that they won
            writing.write("Black Wins!",font =("Arial", 50, "bold"))
            #Set game to false to stop movement
            game = False
            #Create break to stop them from accidently moving one more time and breaking things.
            break
        #Create movement for turtle
        green.forward(random.randint(1,51))
        #If statement to check if they reached the finish line
        if green.xcor() > 499:
            #Print of that they won
            writing.write("Green Wins!",font =("Arial", 50, "bold"))
            #Set game to false to stop movement
            game = False
            #Create break to stop them from accidently moving one more time and breaking things.
            break
        #Create movement for turtle
        red.forward(random.randint(1,51))
        #If statement to check if they reached the finish line
        if red.xcor() > 499:
            #Print of that they won
            writing.write("Red Wins!",font =("Arial", 50, "bold"))
            #Set game to false to stop movement
            game = False
            #Create break to stop them from accidently moving one more time and breaking things.
            break
        #Create movement for turtle
        yellow.forward(random.randint(1,51))
        #If statement to check if they reached the finish line
        if yellow.xcor() > 499:
            #Print of that they won
            writing.write("Yellow Wins!",font =("Arial", 50, "bold"))
            #Set game to false to stop movement
            game = False
            #Create break to stop them from accidently moving one more time and breaking things.
            break
        #Create movement for turtle
        orange.forward(random.randint(1,51))
        #If statement to check if they reached the finish line
        if orange.xcor() > 499:
            #Print of that they won
            writing.write("Orange Wins!",font =("Arial", 50, "bold"))
            #Set game to false to stop movement
            game = False
            #Create break to stop them from accidently moving one more time and breaking things.
            break
        #Create movement for turtle
        purple.forward(random.randint(1,51))
        #If statement to check if they reached the finish line
        if purple.xcor() > 499:
            #Print of that they won
            writing.write("Purple Wins!",font =("Arial", 50, "bold"))
            #Set game to false to stop movement
            game = False
            #Create break to stop them from accidently moving one more time and breaking things.
            break
    #Bring back all of the values found in this function for later use.
    return black, green, red, yellow, orange, purple
#Figure out how to make turtles move at the same time.

#Set vaulues to 0 and call the function so it actually happens
turtles("", "", "", "", "", "")
#Make it so that it won't close until the user decides
turtle.done()