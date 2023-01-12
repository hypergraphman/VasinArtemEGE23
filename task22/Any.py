d = dict()
d['0'] = [0, ['0']]
for line in open('22-28.txt').readlines():
    n, t, x = line.split('\t')
    t = int(t)
    x = x.strip().strip('"').split('; ')
    d[n] = [t, x]
# print(d)

for key in d:
    d[key][0] += d[max(d[key][1], key=lambda x: d[x][0])][0]

print(max(d.values(), key=lambda x: x[0])[0])