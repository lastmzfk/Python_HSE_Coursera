def rec():
    n = int(input())
    if n == 0:
        return n
    return n + rec()


print(rec())
