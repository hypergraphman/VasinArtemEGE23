u = set(range(1, 100))
b = set(range(10, 40 + 1))
d = set(range(6, 100, 6))
not_d = u - d
not_b = u - b
r = not_b | not_d
print(sorted(u - r))