from functools import cache


@cache
def f(n):
    if n < 4:
        return 1
    if n % 2:
        return n
    return f(n - 1) + f(n - 2) + f(n - 3)


for i in range(2000):
    f(i)
print(f(2254) - f(2252))


a = [0, 1, 1, 1] + [0] * 2300
for i in range(4, 2300):
    if i % 2 == 0:
        a[i] = a[i - 1] + a[i - 2] + a[i - 3]
    else:
        a[i] = i
print(a[2254] - a[2252])
