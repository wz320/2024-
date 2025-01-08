from math import gcd
while 1:
    try:
        a,b=map(int,input().split())
        print(gcd(a,b))
    except EOFError:
        break


