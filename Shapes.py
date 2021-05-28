import turtle
import random

scn = turtle.Screen()
scn.colormode(255)

t = turtle.Turtle()
t.hideturtle()
t.speed(350)

t.pu()

shapess = ['circle', "square", 'rectangle', "triangle","star"]


class Shapes():
    def __init__(self, shape, x, y, length, length2, color, fill):
        self.shape = shape
        self.x = x
        self.y = y
        self.length = length
        self.length2 = length2
        self.color = color
        self.fill = fill

    def go(self):
        print('l')
        if str(self.shape) == 'circle':
            t.pencolor(self.color)
            t.fillcolor(self.fill)
            t.goto(self.x, self.y)
            t.pd()
            t.dot((self.length + self.length2) / 2)
            t.pu()
        if str(self.shape) == "square":
            t.fillcolor(self.fill)
            t.pencolor(self.color)
            t.goto(self.x, self.y)
            t.begin_fill()
            t.pd()
            for i in range(4):
                t.fd((self.length + self.length2) / 2)
                t.rt(90)
                t.pd()
            t.end_fill()
            t.pu()
        if str(self.shape) == "rectangle":
            t.fillcolor(self.fill)
            t.pencolor(self.color)
            t.goto(self.x, self.y)
            t.begin_fill()
            t.pd()
            for i in range(2):
                t.fd(self.length)
                t.rt(90)
                t.fd(self.length2)
                t.rt(90)
            t.end_fill()
            t.pu()
        if str(self.shape) == 'triangle':
            t.pencolor(self.color)
            t.fillcolor(self.fill)
            t.goto(self.x, self.y)
            t.begin_fill()
            t.pd()
            t.rt(60)
            t.fd((self.length + self.length2) / 2)
            t.rt(120)
            t.fd((self.length + self.length2) / 2)
            t.rt(120)
            t.fd((self.length + self.length2) / 2)
            t.end_fill()
            t.pu()
        if str(self.shape) == 'star':
            t.pencolor(self.color)
            t.fillcolor(self.fill)
            t.goto(self.x, self.y)
            t.begin_fill()
            t.pd()
            for i in range(5):
                t.rt(40)
                t.fd((self.length + self.length2) / 2)
            t.end_fill()
            t.pu()


for i in range(50):
    s = str(i)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    s = Shapes(random.choice(shapess), random.randint(-300, 300), random.randint(-300, 300), random.randint(10, 100),
               random.randint(10, 100), ((r, g, b)), ((b, g, r)))
    s.go()

turtle.done()
