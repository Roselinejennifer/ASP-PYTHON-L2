import turtle

try:

    color = input("Enter a color: ")

    turtle.color(color)

    turtle.forward(100)

except turtle.TurtleGraphicsError:

    print("Invalid color. Please choose a valid color name or hex code.")
