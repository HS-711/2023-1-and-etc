n=int(input())
tri,dp=[]*n,[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    k=list(map(int,input().split()))
    tri.append(k)
dp[0][0]=tri[0][0]
for row in range(1,n):
    for col in range(0,row+1):
        if col==0:
            dp[row][col]=dp[row-1][col]+tri[row][col]
        elif col==row:
            dp[row][col]=dp[row-1][col-1]+tri[row][col]
        else:
            dp[row][col]=max(dp[row-1][col-1]+tri[row][col],dp[row-1][col]+tri[row][col])
print(max(dp[n-1]))
