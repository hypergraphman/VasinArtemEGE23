def cs(a, base):
    c = ''
    r = 0
    for i in range(len(a)):
        if (int(a[i]) + r) // base == 0:
            c += '0'
        else:
            c += f'{(int(a[i]) + r) // base}'
        r = (int(a[i]) + r) % base
    return int(c + str(r))


p = f'{cs(str(49 ** 7 + 7 ** 21 - 7), 7)}'
print(p.count('6'))
