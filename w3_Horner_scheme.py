n = int(input())
x = float(input())
n1 = n + 1
v = x
nx = n
i = 0
s = 0
while n >= 0:
    a = float(input())
    if nx > 1:
        while nx > 1:
            x *= v
            nx -= 1
    elif nx == 1:
        x = v
    else:
        x = 1
    f = a * x
    s += f
    x = v
    n -= 1
    nx = n
print(s)
