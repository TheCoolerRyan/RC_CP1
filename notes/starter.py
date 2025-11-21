import turtle as t


def draw(length):
    if length > 5:
        for i in range(3):
            turtle.forward(length)
            draw(length / 3)
            turtle.right(180)
            turtle.forward(length)
            turtle.right(60)

turtle = t.Turtle()
turtle.speed(0)
turtle.color("Light Blue")
turtle.penup()
turtle.goto(50,50)
turtle.pendown()

for i in range(6):
    draw(100)
    turtle.right(60)

turtle.hideturtle()
t.done()