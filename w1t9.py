$Echo $PATH
/documents/Python
#!usr/bin/env python3
n=int(input())
e=n%10
s=n//100
d=(n-e)%100//10
print(s+d+e)