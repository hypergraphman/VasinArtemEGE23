for a in range(1000):
    fit = True
    for x in range(1000):
        for y in range(1000):
            if not ((x > 4) or ((x + 2) < y) or ((x * x + y * y) < a)):
                fit = False
                break
        if not fit:
            break
    if fit:
        print(a)