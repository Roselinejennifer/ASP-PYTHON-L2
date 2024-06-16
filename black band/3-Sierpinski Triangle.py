import turtle
def draw_triangle(vertices, color):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(vertices[0][0], vertices[0][1])
    turtle.down()
    turtle.begin_fill()
    turtle.goto(vertices[1][0], vertices[1][1])
    turtle.goto(vertices[2][0], vertices[2][1])
    turtle.goto(vertices[0][0], vertices[0][1])
    turtle.end_fill()


def get_midpoint(point1, point2):
    return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]


def sierpinski(vertices, depth):
    colors = ['blue', 'red', 'green', 'yellow', 'purple', 'orange']
    draw_triangle(vertices, colors[depth % len(colors)])

    if depth > 0:
        mid1 = get_midpoint(vertices[0], vertices[1])
        mid2 = get_midpoint(vertices[1], vertices[2])
        mid3 = get_midpoint(vertices[2], vertices[0])

        sierpinski([vertices[0], mid1, mid3], depth - 1)
        sierpinski([vertices[1], mid1, mid2], depth - 1)
        sierpinski([vertices[2], mid2, mid3], depth - 1)


def main():
    turtle.speed(0)
    turtle.bgcolor("white")

    # Initial vertices of the main triangle
    size = 400
    vertices = [[-size / 2, -size / 2], [0, size / 2], [size / 2, -size / 2]]

    depth = int(input("Enter the depth level: "))

    sierpinski(vertices, depth)

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
