import turtle
try:

    turtle.forward(200)

    turtle.left(90)

    turtle.forward(300)

except turtle.Terminator:

    print("Turtle went off-screen! Resetting position.")

    turtle.penup()

    turtle.goto(0, 0)

    turtle.pendown()

