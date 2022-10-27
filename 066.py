import turtle
import random

for i in range(8):
    randomcolor = random.choice(["red","black","yellow","green","blue","pink"])
    turtle.color(randomcolor)
    turtle.forward(100)
    turtle.left(45)
