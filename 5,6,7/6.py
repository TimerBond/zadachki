from random_sum import random_sum
from random import randint

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


print('Задача 6_1')
s = random_sum()
l = list(str(s))
ans = 0
num = ''
for el in l:
    if el == '+':
        ans += int(num)
        num = ''
    else:
        num += el
print(ans + int(num))

print('\nЗадача 6_2')
a = [4, 5, 2, 3, 4]
print(a)
print('Max:', str(max(a)), 'Min:', str(min(a)))
suma = (sum(a))
print("Sum:", str(suma), "Average:", str(suma / len(a)))
print("Second min:", sorted(a)[-2])

print('\nЗадача 6_3')
stroka = input('Введите слово:\n')
lst = list(stroka)
if lst == lst[-1::-1]:
    print('yes')
else:
    print('no')

print('\nЗадача 6_4')
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(a)
b = []
for el in a:
    if isPrime(el):
        b.append(el)
print(b)

print('\nЗадача 6_5')
n = int(input("Кол-во элементов:\n"))
print('Введите числа:')
m = []
summ = 0
for i in range(n):
    s = input()
    m.append(s)
    summ += int(s)
print('Average:', str(summ / n))

print('\nЗадача 6_6 + 6_7')
m = [randint(-20, 20) for i in range(10)]
print(' '.join(map(lambda x: str(x), m)))
minimum = int(input('Введите минимум: '))
maximum = int(input('Введите максимум: '))
ind = []
k = len(m)
i = 0
j = 0
while i < k:
    if m[i] in range(minimum, maximum + 1):
        if j:
            ind.append(i + j)
        else:
            ind.append(i)
        del m[i]
        k = len(m)
        i -= 1
        j += 1
    i += 1
print('Кол-во индексов:', len(ind))
print('Индексы:', ind)
print("Конечный массив:", m)