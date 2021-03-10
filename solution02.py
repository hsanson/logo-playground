"""
Exercise 02

Objective:
    - Practice logical thiking to draw a shape using line primitives.
    - Understand how function arguments and variables can help reduce code
      duplication and maintenance.
    - Understand how loops can help reduce code duplication and maintenance.

Documentation:
  - https://docs.python.org/3.7/library/turtle.html
"""
import turtle


jim = turtle.Turtle()
canvas = jim.getscreen()


def start():
    reset()
    draw_square(100)


def draw_square(size):
    for _ in range(0, 4):
        jim.forward(size)
        jim.left(90)


def reset():
    jim.reset()
    jim.color('blue')
    jim.pensize(5)
    jim.shape('turtle')


def mainloop():
    canvas.listen()
    canvas.onkey(start, "r")
    canvas.mainloop()


if __name__ == "__main__":
    reset()
    mainloop()
