def f(n):
    step1 = f'{n:b}'
    if sum(map(int, step1)) % 2 == 0:
        step2 = '10' + step1[2:] + '0'
    else:
        step2 = '11' + step1[2:] + '1'
    return int(step2, 2)


for i in range(35, 0, -1):
    if f(i) < 35:
        print(i)
        break
