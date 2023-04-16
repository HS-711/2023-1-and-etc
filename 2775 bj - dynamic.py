t=int(input())
answ=[]
k,n=[0 for _ in range(t)],[0 for _ in range(t)]
for i in range(t):
    k[i]=int(input())
    n[i]=int(input())
for i in range(t):
    f,h=k[i],n[i]
    dp=[[1 for _ in range(h+1)] for _ in range(f+1)]
    for i in range(1,h+1):
        dp[0][i]=i
    for floor in range(1,f+1):
        for ho in range(2,h+1):
            dp[floor][ho]=dp[floor-1][ho]+dp[floor][ho-1]
    answ.append(dp[f][h])
for i in answ:
    print(i)
