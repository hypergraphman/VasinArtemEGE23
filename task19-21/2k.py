start = 3
win = 144


def f(a, b, c, m):
    if a * b >= win:
        return c % 2 == m % 2
    if c == m:
        return False
    moves = [f(a + 1, b, c + 1, m),
             f(a * 2, b, c + 1, m),
             f(a, b + 1, c + 1, m),
             f(a, b * 2, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for ib in range(1, win // start):
    for im in range(1, 5):
        if f(start, ib, 0, im):
            print(ib, im)
            break