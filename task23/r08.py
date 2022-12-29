a = [0] * 13
a[2] = 1
for i in range(2, 8):
    if i + 1 <= 8:
        a[i + 1] += a[i]
    if i + 2 <= 8:
        a[i + 2] += a[i]
    if i * 3 <= 8:
        a[i * 3] += a[i]
print(a[8])
for i in range(8, 10):
    if i + 1 <= 10:
        a[i + 1] += a[i]
    if i + 2 <= 10:
        a[i + 2] += a[i]
    if i * 3 <= 10:
        a[i * 3] += a[i]
print(a[10])
for i in range(10, 12):
    if i + 1 <= 12:
        a[i + 1] += a[i]
    if i + 2 <= 12:
        a[i + 2] += a[i]
    if i * 3 <= 12:
        a[i * 3] += a[i]
print(a[12])