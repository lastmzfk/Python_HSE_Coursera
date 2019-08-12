a = int(input())
b = int(input())
c = int(input())
if a == b and a != c:
    print(2)
elif a == c and a != b:
    print(2)
elif b == c and c != a:
    print(2)
elif a == b == c:
    print(3)
elif a != b and b != c:
    print(0)
else:
    print('biba')
