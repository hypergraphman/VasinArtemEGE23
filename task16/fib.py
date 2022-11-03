from functools import cache


@cache
def fib(x):
    if (x == 1) or (x == 2):
        return 1
    return fib(x - 1) + fib(x - 2)


a = 1
b = 1
for i in range(10 - 2):
    a, b = b, a + b
print(b)