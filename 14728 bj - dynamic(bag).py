n,t=list(map(int,input().split()))
k,s=[0 for _ in range(n)],[0 for _ in range(n)]
for x in range(n):
    k[x],s[x]=list(map(int,input().split()))
dp=[[0 for _ in range(t+1)]for _ in range(n+1)]
for row in range(1,n+1):
    for col in range(1,t+1):
        if k[row-1]>col:
            dp[row][col]=dp[row-1][col]
        else:
            value1=s[row-1]+dp[row-1][col-k[row-1]]
            value2=dp[row-1][col]
            dp[row][col]=max(value1,value2)
print(dp[n][t])
