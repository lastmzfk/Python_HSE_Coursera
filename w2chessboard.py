a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % 2 == 1 and b % 2 == 1 or a % 2 == 0 and b % 2 == 0:
    cell_one = 1
else:
    cell_one = 0
if c % 2 == 1 and d % 2 == 1 or c % 2 == 0 and d % 2 == 0:
    cell_two = 1
else:
    cell_two = 0
if cell_one == cell_two:
    print('YES')
else:
    print('NO')
