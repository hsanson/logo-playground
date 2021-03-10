"""
Solution 04

Objective:
    - Understand the concept of abstraction and how it can be used to reduce
      code duplication and maintenance.

Documentation:
  - https://docs.python.org/3.7/library/turtle.html
"""
import turtle


jim = turtle.Turtle()
canvas = jim.getscreen()


def start():
    reset()
    draw_square(100)
    draw_triangle(100)
    draw_pentagon(100)
    draw_star(100)


def draw_shape(count, size, angle):
    for _ in range(0, count):
        jim.forward(size)
        jim.left(angle)


def draw_square(size):
    draw_shape(4, size, 90)


def draw_triangle(size):
    draw_shape(3, size, 120)


def draw_star(size):
    draw_shape(9, size, 225)


def draw_pentagon(size):
    draw_shape(5, size, 72)


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
