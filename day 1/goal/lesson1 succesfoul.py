from turtle import *


#we want to paint house

#step 1:draw a square

width(7)
color("red")
forward (200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
left(90)

color("yellow")
begin_fill()
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()
 
color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(00, 150)
pendown()

color("blue")
begin_fill()
right(150)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(150, 200)
pendown()
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

exitonclick()