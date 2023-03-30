start = 14
end = 40
over_end = 49


def f(a, b, c, d):
    if end <= a + b <= over_end:
        return c % 2 == d % 2
    if a + b > over_end:
        return (c + 1) % 2 == d % 2
    if c == d:
        return 0
    moves = [f(a + 1, b, c + 1, d),
             f(a * 2, b, c + 1, d),
             f(a, b + 1, c + 1, d),
             f(a, b * 2, c + 1, d)]
    return any(moves) if (c + 1) % 2 == d % 2 else all(moves)


for s in range(1, 26):
    for move_end in range(1, 5):
        if f(start, s, 0, move_end):
            print(s, move_end)
            break