def skobki(s):
    if len(s) == 1 or 0:
        return s
    if len(s) == 2:
        return s
    return s[0] + '*' + skobki(s[1:-1]) + '*' + s[-1]


print(skobki('malina'))
