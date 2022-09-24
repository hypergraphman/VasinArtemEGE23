n = '8' * 70
while '2222' in n or '8888' in n:
    if '2222' in n:
        n = n.replace('2222', '88', 1)
    else:
        n = n.replace('8888', '22', 1)
print(n)