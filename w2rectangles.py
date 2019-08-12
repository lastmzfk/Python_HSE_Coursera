a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('acute')
elif a > b and a > c:
    if a >= c + b:
        print('impossible')
    elif a * a == b * b + c * c:
        print('rectangular')
    elif a * a > b * b + c * c:
        print('obtuse')
    elif a * a < b * b + c * c:
        print('acute')
elif b > c and b > a:
    if b >= c + a:
        print('impossible')
    elif b * b == a * a + c * c:
        print('rectangular')
    elif b * b > a * a + c * c:
        print('obtuse')
    elif b * b < a * a + c * c:
        print('acute')
elif c > a and c > b:
    if c >= a + b:
        print('impossible')
    elif c * c == b * b + a * a:
        print('rectangular')
    elif c * c > b * b + a * a:
        print('obtuse')
    elif c * c < b * b + a * a:
        print('acute')
