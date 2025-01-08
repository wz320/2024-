n=int(input())
total=[]
equal=0
x=0
y=0
z=0
for i in range(n):
    vector=list(map(int,input().split()))
    total.append(vector)
for i in range(n):
    x+=total[i][0]
    y+=total[i][1]
    z+=total[i][2]
if x==y==z==0:
    print('YES')
else:
    print('NO')