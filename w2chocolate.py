n = int(input())
m = int(input())
k = int(input())
s = n * m
if k > s or k < n and k < m:
    print('NO')
elif k % n == 0 or k % m == 0 or s % k == 0:
    print('YES')
elif n % k == 0 or m % k == 0:
    print('YES')
else:
    print('NO')
