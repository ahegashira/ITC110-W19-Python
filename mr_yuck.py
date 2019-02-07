from graphics import GraphWin, Circle, Point, Polygon, color_rgb, Rectangle, Line

win = GraphWin("Remember Mister Yuck?", 600, 600)

# Green Head
head = Circle(Point(299, 299), 250)
head.setFill(color_rgb(90, 255, 84))
head.draw(win)

# Left Eyebrow Polygon
left_brow = Polygon(Point((299-59), (299-139)), Point((299-67), (299-126)), Point((299-134), (299-149)), Point((299-119), (299-179)))
left_brow.setFill('black')
left_brow.draw(win)

# Right Eyebrow Polygon
right_brow = Polygon(Point((299+59), (299-139)), Point((299+67), (299-126)), Point((299+134), (299-149)), Point((299+119), (299-179)))
right_brow.setFill('black')
right_brow.draw(win)

# Left Eye Polygon
left_eye = Polygon(
    Point((299-58),(299-112)), Point((299-75),(299-82)), Point((299-90),(299-100)), Point((299-134),(299-75)), Point((299-141),(299-93)), Point((299-90),(299-120))
)
left_eye.setFill('black')
left_eye.draw(win)

# Right Eye Polygon
right_eye = Polygon(
    Point((299+58),(299-112)), Point((299+75),(299-82)), Point((299+90),(299-100)), Point((299+134),(299-75)), Point((299+141),(299-93)), Point((299+90),(299-120))
)
right_eye.setFill('black')
right_eye.draw(win)

# Mouth - Overlapping Circles
frown = Circle(Point(299, 505), 165)
frown.setFill('black')
frown.draw(win)

frown_cover = Circle(Point(299, 650), 260)
frown_cover.setFill(color_rgb(90, 255, 84))
frown_cover.setWidth(0)
frown_cover.draw(win)

# Tongue - Circle & Polygon Combo with Black Vertical Line
tongue_tip = Circle(Point(299, 405), 30)
tongue_tip.setFill(color_rgb(90, 255, 84))
tongue_tip.setWidth(3)
tongue_tip.draw(win)

tongue = Rectangle(Point(269, 403), Point(329, 348))
tongue.setFill(color_rgb(90, 255, 84))
tongue.setWidth(0)
tongue.draw(win)

tongue_ctr = Line(Point(299, 348), Point(299, 385))
tongue_ctr.setWidth(4)
tongue_ctr.draw(win)

tongue_edge_L = Line(Point(269, 348), Point(269, 410))
tongue_edge_L.setFill('black')
tongue_edge_L.setWidth(3)
tongue_edge_L.draw(win)

tongue_edge_R = tongue_edge_L.clone()
tongue_edge_R.move(60,0)
tongue_edge_R.draw(win)

# Black Border
border = Circle(Point(299,299), 350)
border.setFill('')
border.setWidth(200)
border.draw(win)

win.getMouse()
win.close()