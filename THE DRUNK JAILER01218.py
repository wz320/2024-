import math
lines=int(input())
for i in range(lines):
    n=int(input())
    prisoner=[]
    for j in range(1,n+1):
        if math.sqrt(j)%1==0:
            prisoner.append(j)
    print(len(prisoner))
