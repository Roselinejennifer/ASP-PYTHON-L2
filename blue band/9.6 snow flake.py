import turtle

def draw_snowflake(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3
        for _ in range(6):
            draw_snowflake(t, length, depth - 1)
            t.backward(length)
            t.left(60)

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.color("white")
t.pensize(2)

# Move the turtle to the starting position
t.penup()
t.goto(-350 / 2, 200)
t.pendown()

# Start drawing the snowflake
draw_snowflake(t, 700, 2)

# Hide the turtle and keep the window open
t.hideturtle()
screen.mainloop()
