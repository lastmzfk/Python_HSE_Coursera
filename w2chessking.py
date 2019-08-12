a = int(input())
b = int(input())
c = int(input())
d = int(input())
if c - a == 1 and d - b == 1 or c - a == 0 and d - b == 0:
    print('YES')
elif c - a == 0 and d - b == 1 or c - a == 1 and d - b == 0:
    print('YES')
elif c - a == -1 and d - b == -1 or c - a == 0 and d - b == -1:
    print('YES')
elif c - a == -1 and d - b == 0:
    print('YES')
elif c - a == 1 and d - b == -1 or c - a == -1 and d - b == 1:
    print('YES')
else:
    print('NO')
