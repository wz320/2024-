n=int(input())
for i in range(n):
    ans=0
    s=int(input())
    carda=int(input())
    a=list(map(int,input().split()))
    cardb=int(input())
    b=list(map(int,input().split()))
    for j in a:
        ans+=b.count(s-j)
    print(ans)