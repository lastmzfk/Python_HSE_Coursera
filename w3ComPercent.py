from math import floor, ceil

p = float(input())
x = float(input())
y = float(input())
k = int(input())
i = 1
z = x + y / 100
p2 = z + z * p / 100
x = floor(p2)
y = floor((p2 - x) * 100 + 0.00001)
while i <= k:
    i += 1
    z = x + y / 100
    p2 = z + z * p / 100
    x = floor(p2)
    y = floor((p2 - x) * 100 + 0.00001)
    if i == k:
        break
print(x, y)
