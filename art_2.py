from turtle import Turtle

pipis = Turtle()
pipis.speed(10)
dist = 100
sides = 4
while 1:
    for _ in range(sides):
        pipis.forward(dist)
        pipis.left(360 / sides)
    sides = sides + 1
pipis.screen.mainloop()
