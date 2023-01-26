line = open('input.txt').read()
print(line)

count = 1
mx = 0
for i in range(1, len(line)):
    p1, p2 = line[i - 1], line[i]
    if p1 == p2:
        count += 1
        mx = max(count, mx)
    else:
        count = 1
print(mx)