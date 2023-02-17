with open('26-76.txt') as f:
    a = f.readlines()
a = a[1:]
b = []
for i in range(len(a)):
    # a[i] = tuple(map(int, a[i].split()))
    t = a[i].split()
    b.extend([int(t[0]), -int(t[1])])
# a.sort(key=lambda x: (x[0], x[1]))
b.sort(key=lambda x: abs(x))
# s = 0
# mx = 0
# for i in range(1, len(a)):
#     if a[i - 1][1] < a[i][0]:
#         s += a[i][0] - a[i - 1][1]
#         mx = max(mx, a[i][0] - a[i - 1][1])
# print(s, mx)

n = 1
s = 0
mx = 0
for i in range(1, len(b)):
    if b[i] > 0:
        n += 1
    else:
        n -= 1
    if n == 1:
        s += b[i] + b[i - 1]
        mx = max(mx, b[i] + b[i - 1])
print(s, mx)