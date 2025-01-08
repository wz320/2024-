from bisect import bisect_left
T=int(input())
for _ in range(T):
    n=int(input())
    lst=list(map(int,input().split()))
    woods=[]
    for i in range(n):
        l=lst[2*i]
        w=lst[2*i+1]
        woods.append((l,w))
    woods.sort()
    ws=[woods[i][1] for i in range(n)]
    ws.reverse()
    result=[]
    for i in range(n):
        lo=bisect_left(result,ws[i])
        if lo==len(result):
            result.append(ws[i])
        else:
            result[lo]=ws[i]
    print(len(result))