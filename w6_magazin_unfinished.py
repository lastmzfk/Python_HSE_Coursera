n = int(input())
a = list(map(int, input().split()))
a.sort()
c = []
counter = 0
if a[0] >= n:
    c.append(a[0])
for i in range(1, len(a)):
    if a[i] < n:
        continue
    elif abs(a[i - 1] - a[i]) >= 3:
        c.append(a[i])
s = len(c)
print(s)
