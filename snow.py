from graphics import GraphWin, Point, Circle, Polygon, color_rgb
from random import randint
from time import sleep

win = GraphWin('SNOW', 600, 600)
win.setBackground('blue4')

moon = Circle(Point(70, 50), 120)
moon.setFill('yellow')
moon.draw(win)

mount = Polygon(Point(0, 550), Point(100, 500), Point(200, 580), Point(300, 450), Point(400, 520), Point(500, 490), Point(599, 580), Point(599, 599), Point(0, 599), Point(0, 550))
mount.setFill('black')
mount.draw(win)

for i in range(80):
    star = Circle(Point(randint(0, 599), randint(0, 399)), randint(1, 2))
    star.setFill(color_rgb(randint(240, 255), randint(240, 255), randint(0, 15)))
    star.draw(win)

snowballs = []
for i in range(500):
    snowball = Circle(Point(randint(0,599), randint(0, 599)), randint(1, 5))
    snowball.setFill(color_rgb(randint(190, 255), randint(190, 255), randint(190, 255)))
    # snowball.setFill('white')
    snowball.draw(win)
    snowballs.append(snowball)

for s in range(5000):
    for snowball in snowballs:
        snowball.move(0,randint(1, 3))
        if snowball.getCenter().getY() > 599:
            snowball.undraw()
            snowball.move(0, -600)
            snowball.draw(win)

delay = 0.1
frames = 40

win.getMouse()
