"""
Solution 03

Objective:
    - Practice with adquired knowledge to implement different shapes.
    - Observe patterns in the implementations.

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


def draw_square(size):
    for _ in range(0, 4):
        jim.forward(size)
        jim.left(90)


def draw_triangle(size):
    for _ in range(0, 3):
        jim.forward(size)
        jim.left(120)


def draw_pentagon(size):
    for _ in range(0, 5):
        jim.forward(size)
        jim.left(72)


def draw_star(size):
    for _ in range(0, 9):
        jim.forward(size)
        jim.left(225)


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
