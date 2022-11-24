# from itertools import permutations

data = tuple(map(int, open('17-338.txt').readlines()))
mi = min(data)
ma = 0
# couples = []
count = 0
# for a, b in permutations(data):
#     if (a % 117 == mi) or (b % 117 == mi):
#         count += 1
#         if (a + b) > ma:
#             ma = a + b
for i in range(len(data) - 1):
    if (data[i] % 117 == mi) or (data[i + 1] % 117 == mi):
        count += 1
        if (data[i] + data[i + 1]) > ma:
            ma = data[i] + data[i + 1]
print(count, ma)