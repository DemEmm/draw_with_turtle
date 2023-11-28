from turtle import Turtle
from random import random

pipis = Turtle()
pipis.speed(10)
dist = 50
while 1:
        pipis.forward(dist * random())
        pipis.left(random() * 360)

pipis.screen.mainloop()
