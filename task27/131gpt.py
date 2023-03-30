with open('27-131b.txt') as F:
    N, M, K = map(int, F.readline().split())
    population = []
    for i in range(N):
        row = list(map(int, F.readline().split()))
        population.append(row)


# вычисляем индексы середины квадрата
mid = K // 2

# находим сумму жителей в квадратах с центрами в левом верхнем углу
squares = []
s = sum(sum(population[i][j:j+K]) for i in range(K) for j in range(K))
squares.append(s)

# находим сумму жителей в квадратах с центрами в верхней части
for j in range(1, M-K+1):
    s = squares[-1]
    # вычитаем столбец слева от квадрата
    s -= sum(population[i][j-1] for i in range(mid-K//2, mid+K//2+1))
    # добавляем столбец справа от квадрата
    s += sum(population[i][j+K-1] for i in range(mid-K//2, mid+K//2+1))
    squares.append(s)

# находим сумму жителей в квадратах с центрами в остальных частях
for i in range(1, N-K+1):
    s = squares[(i-1)*(M-K+1)]
    # вычитаем строку сверху от квадрата
    s -= sum(population[i-1][j] for j in range(mid-K//2, mid+K//2+1))
    # добавляем строку снизу от квадрата
    s += sum(population[i+K-1][j] for j in range(mid-K//2, mid+K//2+1))
    # находим сумму жителей в квадратах в середине строки
    for j in range(1, M-K+1):
        # вычитаем столбец слева от квадрата
        s -= sum(population[x][j-1] for x in range(i, i+K))
        # добавляем столбец справа от квадрата
        s += sum(population[x][j+K-1] for x in range(i, i+K))
        squares.append(s)

# находим максимальную сумму жителей в квадратах
max_population = max(squares)

print(max_population)