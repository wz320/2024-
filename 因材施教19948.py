n,m=map(int,input().split())
r=list(map(int,input().split()))
r.sort()
d=[]
classes=[]
ans=0
for i in range(len(r)-1):
    d1=r[i+1]-r[i]
    d.append([d1,i])
d.sort(key=lambda x:x[0],reverse=True)
d2=d[:m-1]
d2.sort(key=lambda x:x[-1])
classes.append(r[:d2[0][-1]+1])
classes.append(r[d2[-1][-1]+1:])
for i in range(len(d2)-1):
    classes.append(r[d2[i][-1]+1:d2[i+1][-1]+1])
for i in range(len(classes)):
    ans+=abs(classes[i][-1]-classes[i][0])
print(ans)