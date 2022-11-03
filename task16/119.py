def f(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return 1 + f(n - 1)
    return f(n // 2)


count = 0
for i in range(1, 5 * 10 ** 2 + 1):
    if f(i) == 4:
        count += 1
        print(i, f'{i:b}')
print(count)