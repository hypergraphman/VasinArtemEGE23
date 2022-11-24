data = tuple(map(int, open('17-328.txt').readlines()))

data50 = tuple(filter(lambda x: x % 50 == 0, data))
avg50 = sum(data50) / len(data50)
k = 0
mn = 10**10
for i in range(2, len(data)):
    e1, e2, e3 = data[i - 2], data[i - 1], data[i]
    s1, s2, s3 = e1 + e2, e1 + e3, e2 + e3
    f = lambda x: int(x**0.5)**2 == x
    if f(s1) and f(s2) and f(s3) and min(s1, s2, s3) > avg50:
        mn = min(e1 + e2 + e3, mn)
        k += 1
print(k, mn)
