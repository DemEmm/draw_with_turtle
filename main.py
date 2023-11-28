from turtle import Turtle

pipis = Turtle()
dist = 100
c = 1
while 1:
    for x in range(4):
        for _ in range(0, 10):
            if c == 1:
                pipis.penup()
                c = 0
            else:
                pipis.down()
                c = 1
            pipis.forward(dist / 10)
        pipis.left(90)
    dist = dist - 2
pipis.screen.mainloop()
