m,n,p,q=map(int,input().split())
square=[]
core=[]
ans=[]
for i in range(m):
    line=list(map(int,input().split()))
    square.append(line)
for i in range(p):
    line=list(map(int,input().split()))
    core.append(line)
for i in range(m-p+1):
    line=[]
    for j in range(n-q+1):
        sum_=0
        for k in range(p):
            for l in range(q):
                sum_+=square[i+k][j+l]*core[k][l]
        line.append(sum_)
    ans.append(line)
for i in range(len(ans)):
    print(' '.join(map(str,ans[i])))