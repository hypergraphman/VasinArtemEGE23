with open('27-b.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    data = list(map(int, f.readlines()))

mx = -10**20
l_mx = -10**20
# temp = data[:k]
for i in range(n - k - 1):
    # x = temp[i % k]
    # if x > l_mx:
    #     l_mx = x
    # if l_mx + data[i] > mx:
    #     mx = l_mx + data[i]
    # temp[i % k] = data[i]
    if data[i] > l_mx:
        l_mx = data[i]
    if l_mx + data[i + k + 1] > mx:
        mx = l_mx + data[i + k + 1]
print(mx)
