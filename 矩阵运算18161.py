A=[]
B=[]
S=[]
C=[]
s1=0
s2=[]
ans1=0
ans2=[]
answer=[]
rowA,colA=map(int,input().split())
for i in range(rowA):
    a=list(map(int,input().split()))
    A.append(a)
rowB,colB=map(int,input().split())
if rowB!=colA:
    print('Error!')
    exit()
for i in range(rowB):
    b=list(map(int,input().split()))
    B.append(b)
for i in range(rowA):
    for j in range(colB):
        for k in range(colA):
            s1+=A[i][k]*B[k][j]
        s2.append(s1)
        s1=0
    S.append(s2)
    s2=[]
rowC,colC=map(int,input().split())
if rowC!=rowA or colC!=colB:
    print('Error!')
    exit()
for i in range(rowC):
    c=list(map(int,input().split()))
    C.append(c)
for i in range(rowC):
    ans2=[]
    ans1=0
    for j in range(colC):
        ans1=S[i][j]+C[i][j]
        ans2.append(ans1)
    answer.append(ans2)
for i in range(rowC):
    print(' '.join(map(str,answer[i])))