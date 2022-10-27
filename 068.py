import turtle
import random

ranges = random.randint(10,100)

for i in range(ranges):
    colors = random.choice(["red","black","green","blue","pink",])
    mm = random.randint(10,100)
    rkreh = random.randint(20,360)
    turtle.color(colors)
    turtle.forward(mm)
    turtle.left(rkreh)
