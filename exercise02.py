"""
Exercise 02

Task:
    - Use forward(), right(), and left() methods to implement a
      draw_square() method that draws a square shape.
    - Change the size of the square drawn by modifying the argument
      to the forward(), right(), and left() methods.
    - Make use of method arguments to set square size.
    - Make use of loops to reduce duplicated code.

Optional:
    - Draw multiple squares of different sizes.


Documentation:
  - https://docs.python.org/3.7/library/turtle.html
"""
import turtle


jim = turtle.Turtle()
canvas = jim.getscreen()


def start():
    reset()
    draw_square()


def draw_square():
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
