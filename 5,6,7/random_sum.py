def random_sum():
    from random import randint
    n = int(input('Введите количество чисел:\n'))
    a = ''
    for i in range(n):
        a += str(randint(0, 100))
        if i != n - 1:
            a += '+'
    print('Строка:\n' + a)
    return a