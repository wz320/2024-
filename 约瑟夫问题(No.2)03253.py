while True:
    n,p,m=map(int,input().split())
    ans=[]
    if {n,p,m}=={0}:
        break
    people=[x for x in range(1,n+1)]
    people=people[p-1:]+people[:p-1]
    while len(people)>0:
        for i in range(m-1):
            people.append(people.pop(0))
        ans.append(people.pop(0))
    ans=map(str,ans)
    print(','.join(ans))