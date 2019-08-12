n = int(input())
i = 0
a = 0
z = 0
x = 1
while n != 0:
    if n == a:
        z += 1
        if x < z:
            x = z
    elif n != a:
        z = 1
    a = n
    n = int(input())
print(x)
