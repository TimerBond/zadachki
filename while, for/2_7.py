n = int(input("Введите n: "))
for i in range(n):
    a = i * i
    c = i
    b = 0
    j = 0
    while a % 10 == c % 10 and c != 0:
        b += (a % 10) * (10 ** j)
        j += 1
        a //= 10
        c //= 10
    if b * b == i*i:
        print(str(i) + ":", b, "*", b, "=", i * i)