with open('26-97.txt') as f:
    n = int(f.readline())
    a = []
    for s in f.readlines():
        t, t1 = map(int, s.split())
        a.append((t, t - t1 * 2 - 3))
a.sort(key=lambda x: (x[0], x[1]))
d = a[0][0]
res_2 = d
res = 1
i = 1
print(*a)
while i < n:
    if d <= a[i][1]:
        res += 1
        d = a[i][0]
        print(d)
    i += 1

print(res, res_2)