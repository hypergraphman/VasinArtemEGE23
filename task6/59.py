from turtle import *

speed(0)
cell = 40

for _ in range(4):
    for _ in range(3):
        forward(2 * cell)
        right(270)
    forward(5 * cell)

penup()
for x in range(-10 * cell, 11 * cell, cell):
    for y in range(-10 * cell, 11 * cell, cell):
        goto(x, y)
        dot(6)

done()
