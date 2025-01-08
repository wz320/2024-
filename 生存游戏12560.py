n,m=map(int,input().split())
matrix=[[0]*(m+2)]
output=[]
for i in range(n):
    row=[0]
    row.extend(list(map(int, input().split())))
    row.append(0)
    matrix.append(row)
a=[0]*(m+2)
matrix.append(a)
for i in range(1,n+1):
    row1=[]
    for j in range(1,m+1):
        neibor=matrix[i-1][j-1]+matrix[i-1][j]+matrix[i-1][j+1]+matrix[i][j-1]+matrix[i][j+1]+matrix[i+1][j-1]+matrix[i+1][j]+matrix[i+1][j+1]
        if neibor<2:
            row1.append(0)
        elif neibor==2:
            row1.append(matrix[i][j])
        elif neibor==3:
            row1.append(1)
        elif neibor>3:
            row1.append(0)
    output.append(row1)
for i in range(n):
    print(' '.join(map(str,output[i])))