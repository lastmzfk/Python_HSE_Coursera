a = int(input())
b = int(input())
c = int(input())
if a > b >= c or a > c > b:
    print(a)
elif b > c > a or b > a >= c:
    print(b)
else:
    print(c)
