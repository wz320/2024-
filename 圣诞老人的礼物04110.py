n,maxw=map(int,input().split())
total=[]
weight=0
ans=0
for i in range(n):
    v,w=map(int,input().split())
    price=v/w
    total.append([price,v,w])
total.sort(reverse=True)
for i in total:
    if weight+i[-1]>maxw:
        ans=ans+i[0]*(maxw-weight)
        break
    else:
        ans+=i[1]
        weight+=i[-1]
print(f'{ans:.1f}')