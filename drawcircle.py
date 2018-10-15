import sys, random, argparse
import numpy as np
import math
import turtle
import random
from PIL import image
from datetime import datetime
from fractions import gcd

def drawCircleTurtle(x, y, r):
    turtle.up()
    turtle.setpos(x+r, y)
    turtle.down()

    for i in range (0, 365, 1):
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))


drawCircleTurtle(100,100,100)
turtle.mainloop()

# git test
# git test 2
# git test 3

# a class that draws a Sprograph
class Spiro:
    # Constructor
    def __init__(self, xc, yc, col, R, r, l):
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.step = 5
        self.drawingComplete = False

        self.setparams(xc, yc, col, R, r, l)

        self.restart()

    def setParams(self, cx, yc, col, R, r, l):
        self.xc = xc
        self.yc = yc
        self.R - int(R)
        self.r = int(r)
        self.l = l
        self.col = col

        # reduce r/R to its smalles form by dividing with the GCD
        gcdVal = gcd(self.r, self.R)
