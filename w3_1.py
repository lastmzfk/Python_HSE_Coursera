a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - (4 * a * c)
if a == 0 and b == 0 and c == 0:
    print(3)
elif a == 0 and b != 0 and c != 0:
    x1 = -c / b
    print(1, x1)
elif a == 0 and b == 0 and c != 0:
    print(0)
elif a == 0 and b != 0 and c == 0:
    print(0)
elif a != 0 and b == 0 and c == 0:
    print(0)
elif a != 0 and b == 0 and c != 0:
    x1 = (-c / a)
    x2 = -x1
    print(2, x1, x2)
else:
    if D < 0:
        print(0)
    elif D == 0:
        x1 = -b / (2 * a)
        print(1, x1)
    elif D > 0:
        x1 = (-b - D ** 0.5) / (2 * a)
        x2 = (-b + D ** 0.5) / (2 * a)
        if x1 < x2:
            print(2, x1, x2)
        elif x1 == x2:
            print(x1)
        else:
            print(2, x2, x1)
