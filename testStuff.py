import turtle
import math

def drawCircleTurtle(x, y, r):
    turtle.up()
    turtle.setpos(x+r, y)
    turtle.down()

    for i in range (0, 365, 1):
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))


drawCircleTurtle(500,100,100)
turtle.mainloop()


# def drawCircleTurtle(x, y, r):
#     turtle.Turtle().up()
#     turtle.Turtle().setpos(x+r, y)
#     turtle.Turtle().down()
#
#     for i in range (0, 365, 1):
#         a = math.radians(i)
#         turtle.Turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))
#
#
# drawCircleTurtle(100,100,100)
# turtle.mainloop()