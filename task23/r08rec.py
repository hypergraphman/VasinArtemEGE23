def f(star, end):
    if star == end:
        return 1
    if star > end:
        return 0
    return f(star + 1, end) + f(star + 2, end) + f(star * 3, end)


print(f(2, 8) * f(8, 10) * f(10, 12))