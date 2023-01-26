from re import fullmatch

# res = []
# x = ''
# y = '0'
# num = f'32{x}54{y}123'
# while int(num) < 10 ** 13:
#     if (len(num) % 2 == 0) and ('0' not in num) and\
#             (sum(map(int, num[:len(num) // 2])) == sum(map(int, num[len(num) // 2:]))):
#         if int(num) % 519 == 0:
#             res.append((int(num), int(num) // 519))
#     y = str(int(y) + 1)
#     if y == '10':
#
for x in range(10):
    for i in range(0, 10**5):
        t = '32' + str(i) + '54' + str(x) + '123'
        if (int(t) % 519 == 0 and len(t) % 2 == 0 and t.count('0') == 0 and
           sum(map(int, t[:len(t) // 2])) == sum(map(int, t[len(t) // 2:]))):
            print(int(t), int(t) // 519)