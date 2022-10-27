def rev(a, base):
    c = 0
    for i in range(len(a)):
        c += base ** (len(a) - i - 1) * int(a[i])
    return c


p = 0
su = 0
for i in range(15):
    f = f'123{i}5'
    s = f'1{i}233'
    su = rev(f, 15) + rev(s, 15)
    if su % 14 == 0:
        p = i
        break
print(su // 14)