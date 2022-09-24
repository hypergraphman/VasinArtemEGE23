from turtle import *

speed(0)
cell = 40
left(90)

for _ in range(7):
    forward(10 * cell)
    right(120)

penup()
for x in range(0 * cell, 11 * cell, cell):
    for y in range(0 * cell, 11 * cell, cell):
        goto(x, y)
        dot(6)

done()
