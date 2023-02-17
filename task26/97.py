with open('26-97.txt') as f:
    n = int(f.readline())
    a = []
    for s in f.readlines():
        t, t1 = map(int, s.split())
        a.append((t, t - t1 * 2 - 3))
a.sort(key=lambda x: -x[1])

print(*a, sep='\n')
c = 1
p = None
t = a[0]
for el in a:
    if t[1] >= el[0]:
        c += 1
        p = t
        t = el
print(c, max(filter(lambda x: x[0] <= p[1], a)))