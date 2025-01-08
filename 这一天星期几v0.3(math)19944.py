import math
n=int(input())
for i in range(n):
    date=input()
    c=int(date[0:2])
    y=int(date[2:4])
    m=int(date[4:6])
    d=int(date[6:8])
    if m==1 or m==2:
        m+=12
        y=y-1
    if y<0:
        c=c-1
        y+=100
    w=(y+math.floor(y/4)+math.floor(c/4)-2*c+math.floor((26*(m+1))/10)+d-1)%7
    if w==0:
        print('Sunday')
    elif w==1:
        print('Monday')
    elif w==2:
        print('Tuesday')
    elif w==3:
        print('Wednesday')
    elif w==4:
        print('Thursday')
    elif w==5:
        print('Friday')
    elif w==6:
        print('Saturday')