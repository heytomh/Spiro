import math
import turtle

def drawCircleTurtle(x, y, r):
    turtle.up()
    turtle.setpos(x+r, y)
    turtle.down()

    for i in range (0, 365, 1):
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))


drawCircleTurtle(100,100,500)
turtle.mainloop()

# git test
# git test 2
# git test 3