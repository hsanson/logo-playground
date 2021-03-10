"""
Exercise 01

Tasks:
    - Read documentation on move commands forward(), backward(), left(), and right().
    - Use these methods in the draw_lines() method to learn their use.
    - Optionally learn about penup() and pendown() methods.

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
