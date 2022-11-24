data = list(map(int, open('17.txt').readlines()))
mi = 10001
ma = -100000
count = 0
for i in range(len(data)):
    if (data[i] % 10 == 7) and (data[i] < mi):
        mi = data[i]
for i in range(len(data) - 1):
    a = data[i]
    b = data[i + 1]
    if ((a % 10 == 7) != (b % 10 == 7)) and ((a * a + b * b) < mi**2):
        count += 1
        if (a * a + b * b) > ma:
            ma = a * a + b * b
print(count, ma)
