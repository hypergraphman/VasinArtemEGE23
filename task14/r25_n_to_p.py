from string import digits, ascii_uppercase


def n_to_p(n, p):
    alf = digits + ascii_uppercase
    r = ''
    while n != 0:
        r = alf[n % p] + r
        n //= p
    return r


print(n_to_p(49**7 + 7**21 - 7, 7).count('6'))
