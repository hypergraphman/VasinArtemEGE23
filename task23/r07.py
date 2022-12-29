a = [0] * 30
a[2] = 1
for i in range(2, 14):
    if i + 1 <= 14:
        a[i + 1] += a[i]
    if i * 2 <= 14:
        a[i * 2] += a[i]
for i in range(14, 29):
    if i + 1 <= 29 and i + 1 != 25:
        a[i + 1] += a[i]
    if i * 2 <= 29 and i * 2 != 25:
        a[i * 2] += a[i]
print(a[29])


def f(star, end):
    if star == 25:
        return 0
    if star == end:
        return 1
    if star > end:
        return 0
    return f(star + 1, end) + f(star * 2, end)


print(f(2, 14) * f(14, 29))