from functools import lru_cache


@lru_cache
def divs(n):
    s = {1, n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            s.add(d)
            s.add(n // d)
    return sorted(s)


print(divs(100), len(divs(100)))