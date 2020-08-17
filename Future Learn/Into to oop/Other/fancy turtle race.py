from turtle import Turtle
from random import  randint
from shapes import Paper, Triangle, Rectangle, Oval









laura = Turtle()

laura.color("red")
laura.shape("turtle")

laura.penup()
laura.goto(-160,100)
laura.pendown()

rik =   Turtle()
lauren  =   Turtle()
Karren  =   Turtle()



rik.color("green")
rik.shape("turtle")
rik.penup()
rik.goto(-160,70)
rik.pendown()


lauren.color("blue")
lauren.shape("turtle")
lauren.penup()
lauren.goto(-160,40)
lauren.pendown()


Karren.color("orange")
Karren.shape("turtle")
Karren.penup()
Karren.goto(-160,0)
Karren.pendown()


for movement in range(100):
    laura.forward(randint(1,5))
    rik.forward(randint(1,5))
    lauren.forward(randint(1,5))
    Karren.forward(randint(1,5))




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
