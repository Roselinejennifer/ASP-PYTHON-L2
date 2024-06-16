import turtle
def draw_stop_sign():

    turtle.speed(3)
    turtle.penup()


    turtle.goto(0, -100)
    turtle.pendown()


    turtle.color("black","red")
    turtle.begin_fill()
    for _ in range(8):
        turtle.forward(100)
        turtle.left(45)
    turtle.end_fill()


    turtle.color("white")
    turtle.pensize(5)
    for _ in range(8):
        turtle.forward(100)
        turtle.left(45)


    turtle.penup()
    turtle.goto(40, -20)
    turtle.pendown()
    turtle.color("white")
    turtle.write(" STOP", align="center", font=("Arial", 50, "bold"))


    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    draw_stop_sign()