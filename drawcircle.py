import sys
import random
import argparse
import numpy as np
import math
import turtle
import random
from PIL import Image
from datetime import datetime

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
# turtle.Screen().mainloop()

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

        self.setParams(xc, yc, col, R, r, l)

        self.restart()

    def setParams(self, cx, yc, col, R, r, l):
        self.xc = xc
        self.yc = yc
        self.R - int(R)
        self.r = int(r)
        self.l = l
        self.col = col

        # reduce r/R to its smalles form by dividing with the GCD
        gcdVal = math.gcd(self.r, self.R)
        self.nRot = self.r//gcdVal
        self.k = r/float(R)
        self.t.color(*col)
        self.a = 0

    def restart(self):
        self.drawingComplete = False
        self.t.showturtle()
        self.t.up()
        R, k, l = self.R, self.k,  self.l
        a = 0
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)

    def draw(self):
        R, k, l = self.R, self.k, self.l
        a = 0.0
        for i in range(0, 360*self.nRot +1, self.step):
            a = math.radians(i)
            x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
            y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
            self.t.setpos(self.xc + x, self.yc + y)
        self.t.hideturtle()

    def update(self):
        if self.drawingComplete:
            return
        self.a += self.step
        R, k, l = self.R, self.k, self.l
        a = math.radians(self.a)
        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)
        if self.a >= 360*self.nRot:
            self.drawingComplete = True
            self.t.hideturtle()

class SpiroAnimator:
    def __init__(self, N):
        self.deltaT = 10
        # get the window dimensions
        self.width = turtle.Screen().window_width()
        self.height = turtle.Screen().window_height()
        self.spiros = []
        for i in range(N):
            rparams = self.genRandomParams()
            spiro = Spiro(*rparams)
            self.spiros.append(spiro)
            turtle.ontimer(self.update, self.deltaT)

    def genRandomParams(self):
        width, height = self.width, self.height
        R = random.randint(50, min(width, height)//2)
        r = random.randint(10, 9*R//10)
        l = random.uniform(0.1, 0.9)
        xc = random.randint(-width//2, width//2)
        yc = random.randint(-height//2, height//2)
        col = (random.random(),
               random.random(),
               random.random())
        return (xc, yc, col, R, r, l)

    def restart(self):
        spiro.clear()
        rparams = self.genRandomParams()
        spiro.setParams(*rparams)
        spiro.restart()

    def update(self):
        nComplete = 0
        for spiro in selt.spiros:
            spiro.update()
            if spiro.drawingComplete:
                nComplete += 1
        if nComplete == len(self.spiros):
            self.restart()
        turtle.ontimer(self.update, self.deltaT)

    def toggleTurtles(self):
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()

    def saveDrawing():
        turtle.hideturtle()
        dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
        fileName = 'spiro-' + dateStr
        print('saving drawing to %s.eps/png' % filename)
        canvas = turtle.getcanvas()
        canvas.postscript(file = fileName + '.eps')
        img = Image.open(fileName + 'eps')
        img.save(fileName + '.png', 'png')
        turtle.showturtle()

    def main():
        parser = argparse.ArgumentParser(description=descStr)
        parser.add_argument('--sparams',
                            nargs=3,
                            dest='sparams',
                            required=False,
                            help='The three arguments in sparams: R, r, l.')
        args = parser.parse_args()

        # set up the screen width
        turtle.setup(width=0.8)
        turtle.shape('turtle')
        turtle.title("Spirographs!")
        turtle.onkey(saveDrawing, "s")
        turtle.listen()
        turtle.hideturtle()

        if args.sparams:
            params = [float(x) for x in args.sparams]
            col = (0.0, 0.0, 0.0)
            spiro = Spiro(0, 0, col, *params)
            spiro.draw()
        else:
            spiroAnim = SpiroAnimator(4)
            turtle.onkey(spiroAnim.toggleTurtles, "t")
            turtle.onkey(spiroAnim.restart, "space")

        turtle.mainloop()
