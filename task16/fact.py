# def fact(x):
#     if x <= 1:
#         return 1
#     return x * fact(x - 1)
#
#
# print(fact(1000))

res = 1
for i in range(2, 6):
    res *= i
print(res)