n,k=map(int,input().split())
winner=0
lst=list(map(int,input().split()))
lst.sort(reverse=True)
for i in lst:
    if i>=lst[k-1] and i>0:
        winner+=1
    else:
        pass
print(winner)