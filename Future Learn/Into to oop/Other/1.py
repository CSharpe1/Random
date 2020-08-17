from turtle import Turtle
from random import  randint

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

