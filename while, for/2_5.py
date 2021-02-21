min = 1000
n = int(input("Введите n: "))
for i in range(n):
    x = int(input())
    if x < min and x % 2 == 0 and x % 3 != 0:
        min = x
print(min)