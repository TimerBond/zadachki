min = 1000
for i in range(10):
    x = int(input())
    if x < min and x % 2 == 0 and x % 3 != 0:
        min = x
print(min)