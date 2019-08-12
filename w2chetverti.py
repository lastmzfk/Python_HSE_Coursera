odin_x = int(input())
odin_y = int(input())
dva_x = int(input())
dva_y = int(input())
if odin_x == 0 or odin_y == 0 or dva_x == 0 or dva_y == 0:
    print('N/A')
elif odin_x > 0 and odin_y > 0 and dva_x > 0 and dva_y > 0:
    print('YES')
elif odin_x < 0 and odin_y > 0 and dva_x < 0 and dva_y > 0:
    print('YES')
elif odin_x > 0 and odin_y < 0 and dva_x > 0 and dva_y < 0:
    print('YES')
elif odin_x < 0 and odin_y < 0 and dva_x < 0 and dva_y < 0:
    print('YES')
else:
    print('NO')
