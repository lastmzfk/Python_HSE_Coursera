a = int(input())
if a == 1 or a % 10 == 1 and a % 100 != 11:
    print(a, 'korova')
elif 2 <= a % 10 <= 4 and a % 100 > 20 or 2 <= a % 100 <= 4:
    print(a, 'korovy')
else:
    print(a, 'korov')
