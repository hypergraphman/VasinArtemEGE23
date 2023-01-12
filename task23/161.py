from functools import cache


def fib(n):
    if (n == 1) or (n == 2):
        return 1
    return fib(n - 1) + fib(n - 2)


def func(n, n_max):
    if n > n_max:
        return 0
    if n == n_max:
        return 1
    return func(n + 1, n_max) + func(n + 3, n_max) + func(fib(n), n_max)


print(func(6, 21))
