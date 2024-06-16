import turtle

# Function to draw a single triangle
def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.right(120)

# Function to draw a spiro triangle
def draw_spiro_triangle(side_length, depth):
    angle = 360/depth
    for _ in range(depth):
        draw_triangle(side_length)
        turtle.right(angle)

# Set up the turtle
turtle.speed(0)  # Set the speed to maximum

# Draw the spiro triangle
draw_spiro_triangle(100, 10)

# Keep the window open
turtle.done()