import colorgram
from turtle import Turtle
import random

pipis = Turtle()
pipis.penup()
pipis.screen.screensize(400, 400)
screen_x = pipis.screen.screensize()[0]
screen_y = pipis.screen.screensize()[1]
pipis.setpos(-screen_x / 2, -screen_y / 2)

print(screen_x, screen_y)
colors = colorgram.extract('sweet_pic.jpg', 6)

r = colors[0].rgb.r
g = colors[0].rgb.g
b = colors[0].rgb.b
pipis.screen.colormode(255)
while pipis.position()[1] < screen_y / 2:
    while pipis.position()[0] < screen_x / 2:
        rand_index = round(random.random() * (len(colors)-1))
        r = colors[rand_index].rgb.r
        rand_index = round(random.random() * (len(colors)-1))
        g = colors[rand_index].rgb.g
        rand_index = round(random.random() * (len(colors)-1))
        b = colors[rand_index].rgb.b
        pipis.dot(20, (r, g, b))
        pipis.forward(screen_x / 10)
        print(pipis.position()[1])
    pipis.setpos(-screen_x / 2, pipis.position()[1] + screen_y / 10)


# for pos in range(1,10):
#     for temp in range(1,10):
#         pipis.dot(20, (r, g, b))
#         pipis.forward(screen_x/10)
#     pipis.teleport(-screen_x/pos, (-screen_y/2)+40*pos)

pipis.screen.mainloop()
