from turtle import Turtle, Screen
import colorgram
import random

# do the colorgram extraction
colors = colorgram.extract('blops.jpg', 30)
colorlist = []
for item in colors:
    temptup = (item.rgb.r, item.rgb.g, item.rgb.b)
    colorlist.append(temptup)

# initialize section
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.penup()
tim.hideturtle()
tim.speed("fastest")
timx = -300
timy = -300

def drawrow(timx, timy):
    tim.goto(timx, timy)
    for _ in range(10):
        tim.dot(20, random.choice(colorlist))
        timx += 50
        tim.goto(timx, timy)

# movements
for _ in range(10):
    drawrow(timx, timy)
    timy += 50

screen.exitonclick()