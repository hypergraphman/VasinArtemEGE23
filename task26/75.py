with open('26-75.txt') as f:
    a = f.readlines()[1:]
b = []
for i in a:
    q = tuple(map(int, i.split()))
    b += [q[0], -q[1]]
b.sort(key=lambda x: abs(x))
# a.sort(key=lambda x: (x[0], x[1]))
k = 0
mx = 0
s = 0
t = None
for x in b:
    if x > 0:
        k += 1
        mx = max(mx, k)
        if k == 1:
            t = x
    else:
        k -= 1
        if k == 0:
            s += abs(x) - t
            t = None

print(mx, s)
