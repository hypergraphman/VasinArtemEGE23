from functools import lru_cache
from math import gcd


@lru_cache
def divs(n):
    s = set()
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            s.add(d)
            s.add(n // d)
    return sorted(s)


i = 100_000_000
c = 0
while c < 7:
    t = divs(i)
    if len(t) >= 3 and gcd(t[0], t[1]) == 1 and gcd(t[1], t[2]) == 1 and gcd(t[0], t[2]) == 1:
        print(i, t[-1])
        c += 1
    i += 1
