import functools


def moves(h):
    return h + 1, h + 2, h * 3


@functools.cache
def f(h):
    if h >= 65:
        return 'END'
    elif any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    elif any(f(x) == 'P1' for x in moves(h)):
        return 'B1'
    elif any(f(x) == 'B1' for x in moves(h)):
        return 'P2'
    elif all(f(x) == 'P2' for x in moves(h)):
        return 'B2'


for i in range(64, 1, -1):
    print(i, f(i))
