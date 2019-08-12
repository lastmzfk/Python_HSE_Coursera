a = [int(i) for i in input().split()]
c = []
c.append(a[len(a) - 1])
for i in range(len(a) - 1):
    c.append(a[i])
print(*c)
