x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
z = x2 - x1
if z >= 0:
    z = x2 - x1
else:
    z = -(x2 - x1)
if x1 % 2 == 0 and y1 % 2 == 0 or x1 % 2 == 1 and y1 % 2 == 1 and y1 != y2:
    if x2 % 2 == 0 and y2 % 2 == 0 or x2 % 2 == 1 and y2 % 2 == 1:
        if y2 > y1 and z <= y2 - y1:
            if 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8:
                print('YES')
            elif x1 == x2 and y2 > y1 and z <= y2 - y1:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')