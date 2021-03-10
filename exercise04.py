"""
Exercise 04

Task:
    - Implement a draw_shape() method that can draw any of the rectangle,
      triangle, pentagon, and star shapes given different method arguments.
    - Re-implement the draw_rectangle(), draw_triangle(), draw_pentagon(),
      and draw_star() methods using the draw_shape() method.

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


def draw_pentagon(size):
    for _ in range(0, 5):
        jim.forward(size)
        jim.left(72)


def draw_triangle(size):
    for _ in range(0, 3):
        jim.forward(size)
        jim.left(120)


def draw_star(size):
    for _ in range(0, 9):
        jim.forward(size)
        jim.left(225)


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
