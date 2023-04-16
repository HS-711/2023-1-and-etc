n=int(input())
arr=[0]
dp=[0 for _ in range(n+1)]
for _ in range(n):
    arr.append(int(input()))
if n==1:
    print(arr[1])
elif n==2:
    print(arr[1]+arr[2])
else:
    dp[1]=arr[1]
    dp[2]=arr[1]+arr[2]
    for x in range(3,n+1):
        dp[x]=max(dp[x-1],dp[x-3]+arr[x-1]+arr[x],dp[x-2]+arr[x])
    print(max(dp))
