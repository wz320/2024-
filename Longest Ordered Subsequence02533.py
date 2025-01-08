n=int(input())
sub=[1]*n
lst=list(map(int,input().split()))
for i in range(n):
    for j in range(i):
        if lst[i]>lst[j]:
            sub[i]=max(sub[j]+1,sub[i])
print(max(sub))