with open('27-143a.txt') as f:
    n, k = map(int, f.readline().split())
    data = list(map(int, f.readlines()))

d = 68
rs = []
for i in range(n - k):
    x = sum(data[i:i + k])
    rs.append(x)

mx = 0
l_mx = [0] * d
temp = rs[:k]
for i in range(k, len(rs)):
    x = temp[i % k]
    r = rs[i] % d
    if x > l_mx[r]:
        l_mx[r] = x
    if l_mx[r] +