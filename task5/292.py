for x in range(101):
    n = bin(x)[2:]
    if sum(map(int, list(n))) % 2 == 0:
        n = '10' + n[2:] + '0'
    else:
        n = '11' + n [2:] + '1'
    res = 0
    for i in range(len(n) - 1, -1, -1):
        res += 2 ** i * int(n[len(n) - 1 - i])
    if res < 35:
        print(res, x)