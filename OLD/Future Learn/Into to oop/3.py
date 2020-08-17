from shapes import Paper, Triangle, Rectangle, Oval

paper = Paper()

rect1   =   Rectangle()
rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("orange")
rect1.draw()


rect2   =   Rectangle()
rect2.set_width(200)
rect2.set_height(100)
rect2.set_color("yellow")
rect2.set_x(100)
rect2.set_y(100)
rect2.draw()


tri1   =   Triangle(5,5,12,5,20,30)
tri1.set_color("purple")
tri1.set_x(398)
tri1.set_y(500)
tri1.draw()

oval1   =   Oval()
oval1.randomize(25,100)
oval1.draw()


paper.display()
