with open('26-k1.txt') as f:
    n, k = map(int, f.readline().split())
    a = [int(x) for x in f.readlines()]
a.sort(reverse=True)
b = a[:k]
print(a[k])
s = int(sum([0.2 * x for x in b]))
print(s)

