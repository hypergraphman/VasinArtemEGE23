s1 = 0
n = 2023
while n > 1:
    s1 += n * n
    n -= 1
s2 = 0
n = 2019
while n > 1:
    s2 += n * n
    n -= 1
print(s1 - s2)