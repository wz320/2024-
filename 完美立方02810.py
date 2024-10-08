def cube(x):
    return x*x*x
N=int(input())
ans=[]
for i in range(2,N+1):
    for j in range(2,i+1):
        for k in range(j,i+1):
            for l in range(k,i+1):
                if cube(i)==cube(j)+cube(k)+cube(l):
                    ans.append(['Cube = ',str(i),', ','Triple = (',str(j),',',str(k),',',str(l),')'])
for i in ans:
    print(''.join(i))