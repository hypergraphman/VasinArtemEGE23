from turtle import *

speed(0)
cell = 40

for _ in range(5):
    for _ in range(2):
        forward(3 * cell)
        left(45)
        forward(3 * cell)
        right(90)
    right(180)

penup()
for x in range(-10 * cell, 11 * cell, cell):
    for y in range(-10 * cell, 11 * cell, cell):
        goto(x, y)
        dot(6)

done()
