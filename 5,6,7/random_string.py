def random_string():
    from string import ascii_letters
    from random import randint
    n = int(input('Введите длину строки:\n'))
    ascii_letters += '0123456789'
    a = ''
    for i in range(n):
        a += ascii_letters[randint(0, len(ascii_letters) - 1)]
    print('Строка:\n' + '\'' + a + '\'')
    return a