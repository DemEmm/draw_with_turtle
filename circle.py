from turtle import Turtle

pipis = Turtle()
pipis.speed(100)
dist = 200
pipis.circle(dist)
pipis.left(3)
while 1:
    pipis.circle(dist)
    pipis.left(3)

pipis.screen.mainloop()
