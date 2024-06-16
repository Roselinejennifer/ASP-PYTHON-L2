import turtle

def draw_branch(t, length):
    if length < 5:
        return
    else:
        t.forward(length)
        t.left(30)
        draw_branch(t,length - 15)
        t.right(60)
        draw_branch(t,length - 15)
        t.left