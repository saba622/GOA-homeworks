from turtle import *

def draw_square(x, y):
    penup()
    goto(x, y)
    pendown()
    for _ in range(4):
        forward(100)
        right(90)


done()