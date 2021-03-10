"""
Solution 01

Objectives:
    - Learn to read and understand documentation and code.
    - Learn about and experiment with turtle library drawing capabilities.

Documentation:
  - https://docs.python.org/3.7/library/turtle.html
"""
import turtle


jim = turtle.Turtle()
canvas = jim.getscreen()


def start():
    reset()
    draw_lines()


def draw_lines():
    jim.forward(100)
    jim.right(90)
    jim.forward(100)
    jim.right(90)
    jim.forward(100)
    jim.right(90)
    jim.forward(100)
    jim.right(90)


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
