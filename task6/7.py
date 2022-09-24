from turtle import *


def move(x, y):
    global cur_x, cur_y, cell
    cur_x += x * cell
    cur_y += y * cell
    goto(cur_x, cur_y)


speed(0)
cell = 40
cur_x, cur_y = 0, 0

move(10, 10)
move(3, - 6)
move(-9, 3)

penup()
for x in range(0 * cell, 14 * cell, cell):
    for y in range(0 * cell, 11 * cell, cell):
        goto(x, y)
        dot(6)

done()
