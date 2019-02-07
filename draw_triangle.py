from graphics import GraphWin, Polygon, Point, color_rgb
from random import randint

# Create Window
win = GraphWin("Draw Triangle", 600, 600)

# Get 3 clicks
points = []
for i in range(3):
    point = win.getMouse()
    point.draw(win)
    points.append(point)

# Take those 3 Points and Draw a triangle with random fill color
shape = Polygon(*points)
shape.setFill(color_rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
shape.draw(win)

win.getMouse()
win.close()