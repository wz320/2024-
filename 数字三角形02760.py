n=int(input())
triangle=[]
for i in range(n):
    triangle.append(list(map(int,input().split())))
dp=[triangle[-1]]+[[0]*n for _ in range(n-1)]
for i in range(1,n):
    for j in range(n-i):
        dp[i][j]=max(dp[i][j],dp[i-1][j]+triangle[n-i-1][j],dp[i-1][j+1]+triangle[n-i-1][j])
print(dp[-1][0])