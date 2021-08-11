"""
Complex pattern.
https://www.youtube.com/watch?v=3gSidCqutsM
"""
import turtle

jim = turtle.Turtle()
jim.speed(0)
canvas = jim.getscreen()


def petal():
    """
    Draw a single petal
    """
    for _ in range(36):
        jim.forward(5)
        jim.left(3)

    for _ in range(18):
        jim.forward(10)
        jim.right(3)

    jim.right(180)

    for _ in range(18):
        jim.forward(10)
        jim.left(3)

    for _ in range(36):
        jim.forward(5)
        jim.right(3)

    jim.right(180)
    jim.left(9)


jim.begin_fill()

for _ in range(40):
    petal()

jim.fillcolor("Black")
jim.end_fill()

turtle.done()
