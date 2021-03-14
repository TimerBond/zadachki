from random import randint


def bubbleSort(m):
    for i in range(len(m) - 1):
        for j in range(len(m) - 2, i - 1, -1):
            if m[j] > m[j + 1]:
                m[j], m[j + 1] = m[j + 1], m[j]
    return m


def upbubbleSort(m):
    for i in range(len(m) - 1):
        fl = False
        for j in range(len(m) - 2, i - 1, -1):
            if m[j] > m[j + 1]:
                fl = True
                m[j], m[j + 1] = m[j + 1], m[j]
        if not fl:
            break
    return m


def qSort(A, nStart, nEnd):
    if nStart >= nEnd:
        return
    L = nStart
    R = nEnd
    X = A[(L + R) // 2]
    while L <= R:
        while int(str(A[L])[0]) < int(str(X)[0]): L += 1  # разделение
        while int(str(A[R])[0]) > int(str(X)[0]): R -= 1
        if L <= R:
            A[L], A[R] = A[R], A[L]
            L += 1;
            R -= 1
    qSort(A, nStart, R)  # рекурсивные вызовы
    qSort(A, L, nEnd)


print('Задача 7_1')
m = [randint(-100, 100) for i in range(10)]
print(m)
b = False
for el in m:
    if el % 3 == 0:
        b = True
        break
if b:
    print('yes')
else:
    print('no')

print('\nЗадача 7_2')
x = int(input('X:\n'))
m = [randint(0, 4) for i in range(10)]
print(m)
m2 = []
for i in range(len(m)):
    if x == m[i]:
        m2.append(i)
print(' '.join(map(lambda x: str(x), m2)))

print('\nЗадача 7_3')
m = [randint(-100, 100) for i in range(10)]
print(m)
minimum = 0
maximum = 0
flmin = False
flmax = False
for i in range(len(m)):
    if m[i] == min(m) and not flmin:
        minimum = i
        flmin = True
    elif m[i] == max(m) and not flmax:
        maximum = i
        flmax = True
    if flmin and flmax:
        print('Первый минимум по индексу:', minimum)
        print("Первый максимум по индексу:", maximum)
        break

print('\nЗадача 7_4')
m = [randint(-100, 100) for i in range(10)]
print(m)
m = bubbleSort(m)
print(m)

print('\nЗадача 7_5')
m = [randint(1, 100) for i in range(10)]
print(m)
qSort(m, 0, len(m) - 1)
print('Отсортированный', m)

print('\nЗадача 7_6')
m = [randint(1, 100) for i in range(10)]
print("Рандомный массив:", m)
m2 = sorted(m)
print("Отсортированный массив:", m2)
ind = []
for i in range(len(m2)):
    for j in range(len(m)):
        if m[j] == m2[i]:
            ind.append(j)
print(ind)

print('\nЗадача 7_7')
m = [5, 5, 5, 3, 7, 7, 2, 1, 9, 4, 4, 0]
m = bubbleSort(m)
print("Рандомный отсортированный массив:", m)
ans = 0
for i in range(len(m)):
    if m[i] not in m[:i] + m[i + 1:]:
        ans += 1
print('Количество различных чисел:', ans)

print('\nЗадача 7_8')
m = [1, 1, 1, 2, 3, 3, 3, 2, 2, 6, 0, 0, 0, 0, 0, 0, 1, 8, 8, 8, 8]
print(m)
m1 = []
m2 = []
i = 0
num = m[0]
k = 0
while i < len(m):
    if num == m[i]:
        k += 1
        if i == len(m) - 1:
            m1.append(num)
            m2.append(k)
    else:
        m1.append(num)
        m2.append(k)
        k = 1
        num = m[i]
    i += 1
print(m1)
print(m2)

print('\nЗадача 7_9')
m = [randint(1, 100) for i in range(10)]
print(m)
m = upbubbleSort(m)
print(m)

print('\nЗадача 7_10')
m = [randint(1, 100) for i in range(10)]
print(m)
m = upbubbleSort(m)
print(m)
for i in range(len(m) - 1, -1, -1):
    if m[i] in m[:i] + m[i + 1:]:
        print(m[i])
        break

