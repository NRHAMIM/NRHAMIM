import time
from time import sleep
from turtle import *
bgcolor('red')
pensize(10)
fillcolor('black')
begin_fill()
circle(20)
end_fill()
penup()
right(90)
forward(5)
pendown()
fillcolor('black')
begin_fill()
right(60)
for i in range(6):
    forward(50)
    left(60)
end_fill()
penup()
left(150)
forward(39)
left(90)
forward(9)
pendown()
forward(25)
right(60)
forward(15)
left(60)
forward(25)
penup()
backward(25)
right(60)
back(15)
left(60)
backward(25)
left(60)
pendown()
backward(35)
left(120)
forward(80)
penup()
left(40)
forward(30)
left(140)
pendown()
forward(110)
left(60)
forward(40)
right(60)
forward(7)
right(60)
forward(20)
left(60)
forward(40)
penup()
goto(0,0)
left(90)
forward(39)
right(90)
forward(9)
pendown()
forward(25)
left(60)
forward(15)
right(60)
forward(25)
penup()
backward(25)
left(60)
back(15)
right(60)
backward(25)
right(60)
pendown()
backward(35)
right(120)
forward(80)
penup()
right(40)
forward(30)
right(140)
pendown()
forward(110)
right(60)
forward(40)
left(60)
forward(7)
left(60)
forward(20)
right(60)
forward(40)
done()
sleep(30) 
