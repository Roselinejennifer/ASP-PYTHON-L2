import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Smiley Face with Body")

# Create a turtle object for the smiley face
smiley = turtle.Turtle()

# Draw the head (yellow circle)
smiley.penup()
smiley.goto(0, -100)
smiley.pendown()
smiley.color("yellow")
smiley.begin_fill()
smiley.circle(100)
smiley.end_fill()

# Draw the left eye (black circle)
smiley.penup()
smiley.goto(-35, 35)
smiley.pendown()
smiley.color("black")
smiley.begin_fill()
smiley.circle(10)
smiley.end_fill()

# Draw the right eye (black circle)
smiley.penup()
smiley.goto(35, 35)
smiley.pendown()
smiley.color("black")
smiley.begin_fill()
smiley.circle(10)
smiley.end_fill()

# Draw the mouth (semi-circle)
smiley.penup()
smiley.goto(-40, -10)
smiley.setheading(-60)
smiley.width(5)
smiley.pendown()
smiley.circle(50, 120)

# Create a turtle object for the body
body = turtle.Turtle()

# Draw the body (rectangle)
body.penup()
body.goto(-50, -100)
body.pendown()
body.color("blue")
body.begin_fill()
for _ in range(2):
    body.forward(100)
    body.right(90)
    body.forward(150)
    body.right(90)
body.end_fill()

# Draw the arms (lines)
body.penup()
body.goto(-50, -50)
body.pendown()
body.width(10)
body.goto(-100, -50)

body.penup()
body.goto(50, -50)
body.pendown()
body.goto(100, -50)

# Draw the legs (lines)
body.penup()
body.goto(-30, -250)
body.pendown()
body.goto(-30, -300)

body.penup()
body.goto(30, -250)
body.pendown()
body.goto(30, -300)

# Hide the turtles
smiley.hideturtle()
body.hideturtle()

turtle.done()