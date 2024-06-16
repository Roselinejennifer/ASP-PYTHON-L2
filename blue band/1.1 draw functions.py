import turtle
shape = input("what shape do you want to draw(square,triangle,circle)?")
t = turtle.Turtle()
if shape == "shape":
    for i in range(4):
        t.forward(100),
        t.right(90)
elif shape == "triangle":
    for i in range(3):
        t.forward(100)
        t.left(120)
elif shape =="circle":
    t.circle(50)
else:
    print("invalid shape. please choose either square,triangle, or circle.")
turtle.exitonclick()