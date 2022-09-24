from turtle import *

speed(0)
cell = 40

for _ in range(9):
    forward(3 * cell)
    right(45)
    forward(3 * cell)
    left(90)

penup()
for x in range(-10 * cell, 11 * cell, cell):
    for y in range(-10 * cell, 11 * cell, cell):
        goto(x, y)
        dot(6)

done()
