from itertools import product

print('x y z w')
for x, y, z, w in product((0, 1), repeat=4):
    f = (x or y) and (y != z) and not w
    if f:
        print(x, y, z, w)
