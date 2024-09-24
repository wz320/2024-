from math import ceil
while 1:
    N=int(input())
    arrival=float('inf')
    if N==0:
        break
    for i in range(N):
        speed,time=map(int,input().split())
        if time<0:
            continue
        a=ceil((16200/speed)+time)
        arrival=min(arrival,a)
    print(arrival)