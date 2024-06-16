import turtle
try:

    turtle.do_something_unsupported()
except AttributeError:

    print("That method is not supported by the turtle module.")