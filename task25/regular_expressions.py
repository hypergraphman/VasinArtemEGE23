from re import fullmatch

n = 34034
if fullmatch(r'34\d34\d*', str(n)):
    print('ok')
else:
    print('not ok')