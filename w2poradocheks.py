a = int(input())
b = int(input())
c = int(input())
if a != b != c:
    print(0)
elif a == b != c or a == c != b or b == c != a:
    print(2)
elif a == b == c:
    print(3)
else:
    print('biba')
