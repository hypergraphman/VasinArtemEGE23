with open('26-100.txt') as f:
    n, m = map(int, f.readline().split())
    a = list(map(int, f.readlines()))
a.sort()
key = 11
b = [p2 - p1 <= key for p1, p2 in zip(a, a[1:])]
mx = 0
mx1 = 0
for i in range(n - m):
    if all(a[i:i + m - 1]) and a[i] > mx:
        mx = a[i]
        mx1 = a[i + m - 1]
print(mx, mx1)

