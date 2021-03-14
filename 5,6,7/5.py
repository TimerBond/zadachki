from random_string import random_string
from datetime import date
import os
from random_sum import random_sum

a = random_string()

print('Задача 5_1')
print(a[8:])
print(a[:len(a) // 2 - 2] + a[len(a) // 2 + 2:])
print(a[:-5])

print('\nЗадача 5_2')
print(a[-1::-1])

print('\nЗадача 5_3')
print(a[::2])

print('\nЗадача 5_4')
print(a[::2] + a[1::2])

print('\nЗадача 5_5')
today = str(date.today()).replace('-', '/')
print(today[-2:len(today)] + today[4:-2] + today[:4])

print('\nЗадача 5_6')
for path in os.path.abspath(__file__).split('\\'):
    print(path)

print('\nЗадача 5_7')
string_num = random_sum()
print(sum(map(lambda x: int(x), string_num.split('+'))))

print('\nЗадача 5_8')
s = input('Введите строку:\n')
l = len(s)
flag = 1
res = ''
k = 1
for i in range(l // 2):
    if s[i] == s[l - i - 1]:
        k = 1
    else:
        k = 0
    flag *= k
if flag:
    res = 'Палиндром'
else:
    res = 'Не палиндром!'
print(res)

print('\nЗадача 5_9')
names = ['Иван Иванович',
         "Артем Артемович",
         "Петр Петрович",
         "Василий Васильевич",
         "Семен Семенович"]
days = ['день открытых дверей',
        'праздник весны и труда',
        'праздник - Пасха',
        'день собачьего счастья',
        'праздник - день водолаза']
for i in range(5):
    s = 'Уважаемый (ая), {name}'.format(name=names[i]) + '!\n' + \
        'Приглашаем Вас на {day}'.format(day=days[i]) + '\n' + \
        'Дата события: ' + str(i + 1) + ' мая.' + '\n' + \
        'С уважением, Василий.\n'
    print(s)
