from functools import cache


@cache
def f(n):
    if n == 0:
        return 0
    return f(n - 1) + n


# for i in range(1134567100):
#     f(i)
# count = 0
# for i in range(237567892, 1134567005):
#     if f(i) % 3:
#         count += 1
# print(count)
for i in range(10):
    print(f(i), '\t', i)