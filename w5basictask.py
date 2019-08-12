data = []
while True:
    inp = input()
    if inp == 'end':
        break
    data.append(inp.split())

ln = len(data)
lj = len(data[0])
a = [[0 for j in range(lj)] for i in range (ln)]
for i in range(ln):
    for j in range(lj):
        a1 = i - 1
        if a1 == -1:
            a1 = len(data) - 1
        a2 = i + 1
        if a2 == len(data):
            a2 = 0
        b1 = j - 1
        if b1 == -1:
            b1 = len(data[0]) - 1
        b2 = j + 1
        if b2 == lj:
            b2 = 0
        p1 = int(data[a1][j])
        p2 = int(data[a2][j])
        p3 = int(data[i][b1])
        p4 = int(data[i][b2])
        psum = p1 + p2 + p3 + p4
        a[i][j] = psum
for i in range (ln):
    for j in range(lj):
        print(a[i][j], end=' ')
    print()
