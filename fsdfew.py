
from turtle import *
k = 20
left(90)
tracer(10)
for i in range(2):
    forward(9 * k)
    right(90)
    forward(15 * k)
    right(90)
up()
forward(12 * k)
right(90)
down()
for i in range(2):
    forward(6 * k)
    right(90)
    forward(12 * k)
    right(90)
up()
pu()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5, "red")
        dot(2, "White")
mainloop()
