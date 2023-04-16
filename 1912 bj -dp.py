'''
n=int(input())
n_list=list(map(int,input().split()))
dp=[[0 for _ in range(n+1)]for _ in range(n+1)]
for row in range(1,n+1):
    for col in range(row,n+1):
        if (dp[row-1][col-1]+n_list[col-1])>dp[row][col-1]:
            
        else:
            dp[row][col]=max(dp[row-1][col-1]+n_list[col-1],dp[row][col-1])
print(dp)
print(dp[-1][-1])
'''
n=int(input())
n_list=[0]+list(map(int,input().split()))
dp=[-10001]*(n+1)

for i in range(1,n+1):
    dp[i]=max(n_list[i],n_list[i]+dp[i-1])
print(max(dp))
