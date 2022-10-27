lst = []
for num in range(55):
    f = int('z', 36) * 55**3 + num * 55**2 + int('y', 36) * 55 + int('x', 36)
    s = 2 * 55**3 + int('x', 36) * 55**2 + num * 55 + int('y', 36)
    su = f - s
    if su % 29 == 0:
        print(num)
        lst.append(su)
print(max(lst) - min(lst))
