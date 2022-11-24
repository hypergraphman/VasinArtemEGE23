data = tuple(map(int, open('17.txt').readlines()))
mn = 1000000
for el in data:
    if abs(el) % 10 == 7 and mn > el:
        mn = el
c = 0
mn = mn ** 2
mx = -100000
for i in range(1, len(data)):
    p1, p2 = data[i - 1], data[i]
    s = p1 ** 2 + p2 ** 2
    if ((abs(p1) % 10 == 7) != (abs(p2) % 10 == 7)) and (s < mn):
        c += 1
        mx = max(s, mx)
print(c, mx)