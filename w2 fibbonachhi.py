n = int(input())
a = 0
b = 1
c = b + a
i = 1
while i < n:
    c += b
    b += a
    a = c - b
    i += 1
    if i == n:
        break
print(b)
