n = int(input())
a = 0
b = 1
c = b + a
i = 1
while b <= n:
    c += b
    b += a
    a = c - b
    i += 1
    if c > n > b:
        break
    if b == n:
        break
if n > b or n < b:
    print(-1)
elif n == b:
    print(i)
