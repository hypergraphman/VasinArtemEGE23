def n_to_2(n):
    if n == 0:
        return ''
    return n_to_2(n // 2) + str(n % 2)


# n = int(input())
#
#
# r = ''
# while n != 0:
#     r = str(n % 2) + r
#     n //= 2
# print(r)
print(n_to_2(100))