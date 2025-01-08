m=int(input())
ans=0
for i in range(m):
    ans=0
    a,b,c,d=map(int,input().split())
    for j in [a,-a]:
        for k in [b,-b]:
            for l in [c,-c]:
                for m in [d,-d]:
                    if j+l+k+m==24:
                        ans+=1
                    else:
                        pass
    if ans>0:
        print('YES')
    else:
        print('NO')
