from functools import cache


def func(n, n_max, c=''):
    if n > n_max:
        return 0
    if n == n_max:
        print(c)
        return 1
    return func(n + 1, n_max, c + '1') + func(n + 5, n_max, c + '2') + func(n * 3, n_max, c + '3')


i = 19
while func(1, i) < 175:
    i += 1
print(i)