a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a <= 0 or b <= 0 or c <= 0 or d <= 0 or e <= 0:
    print('NO')
elif a <= d and b <= e or a <= e and b <= d:
    print('YES')
elif a <= d and c <= e or a <= e and c <= d:
    print('YES')
elif b <= d and c <= e or b <= e and c <= d:
    print('YES')
else:
    print('NO')
