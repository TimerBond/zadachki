for i in range(100, 10000):
    a = 0
    if i < 1000:
        a = (i // 100) ** 3 + ((i // 10) % 10) ** 3 + (i % 10) ** 3
    else:
        a = (i // 1000) ** 4 + ((i // 100) % 10) ** 4 + ((i // 10) % 10) ** 4 + (i % 10) ** 4
    if a == i:
        print(i)
