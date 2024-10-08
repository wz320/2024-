import math
while True:
    n1,n2,n3,n4,n5,n6=map(int,input().split())
    nt=0
    if {n1,n2,n3,n4,n5,n6}=={0}:
        break
    nt+=math.ceil(n3/4)+n4+n5+n6
    if n3%4==0:
        if n2>5*n4:
            nt+=math.ceil((n2-n4*5)/9)
    else:
        if n2>(7-2*(n3%4)+n4*5):
            nt+=math.ceil((n2-(7-2*(n3%4)+n4*5))/9)
    if n1>(nt*36-n6*36-n5*25-n4*16-n3*9-n2*4):
        nt+=math.ceil((n1-(nt*36-n6*36-n5*25-n4*16-n3*9-n2*4))/36)
    print(nt)