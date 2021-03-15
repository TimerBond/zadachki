from pprint import pprint
from random import randint
print("8_0:")
m = [[-8, -14, -19, -18],
     [25, 28, 26, 20],
     [11, 18, 20, 25],
     [26, -100, -200, 3]]
print(m)
print(m[1][3])
print(m[2][0])
print('2 метеостанция:')
for i in range(len(m[1])):
    print(i + 1, 'день:', m[1][i])
print("Средняя температура за 3 день:", sum(m[2]) / len(m[2]))
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] in range(24, 27):
            print('На', i + 1, 'метеостанции температура за', j + 1, 'день была:', m[i][j])

print("\n8_1:")
maxi = -100000000
maxind = 0
minind = 0
mini = 100000000
for i in range(len(m)):
    maxj = max(m[i])
    minj = min(m[i])
    if maxj > maxi:
        maxi = maxj
        for j in range(len(m[i])):
            if m[i][j] == maxi:
                maxind = [i, j]
                break
    if minj < mini:
        mini = minj
        for j in range(len(m[i])):
            if m[i][j] == mini:
                minind = [i, j]
                break
print(mini, minind)
print(maxi, maxind)

print("\n8_2:")
summa = -10000000
ans = []
for el in m:
    p = sum(el)
    if p > summa:
        summa = p
        ans = el
print(", ".join(map(lambda x: str(x),ans)))

print("\n8_3:")
n = int(input("Введите размер массива N*N:\n"))
m = [[0 for j in range(n)] for i in range(n)]
minimum = 10000000
pr = 1
for i in range(n):
    l = n - i - 1
    for j in range(n):
        m[i][j] = randint(-100, 100)
        if j > l:
            if m[i][j] < minimum:
                minimum = m[i][j]
        if i == n - 1 and m[i][j] != 0:
            pr *= m[i][j]
pprint(m)
print(minimum)
print(pr)
