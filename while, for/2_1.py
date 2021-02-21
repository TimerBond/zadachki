sump = 0
sumn = 0
x = int(input())
while x != 0:
    if x > 0:
        sump += x
    else:
        sumn += x
    x = int(input())
print("Positive sum =", sump)
print("Negative sum =", sumn)
