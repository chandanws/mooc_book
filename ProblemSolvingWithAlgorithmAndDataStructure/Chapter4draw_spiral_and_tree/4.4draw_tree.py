import turtle


def tree(branch_len, t, pensize):
    if branch_len > 5:
        t.pensize(pensize)
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t, pensize / 2)
        t.left(40)
        tree(branch_len - 15, t, pensize / 2)
        t.right(20)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(75, t, 10)
    my_win.exitonclick()


main()
