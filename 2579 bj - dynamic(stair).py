n=int(input())
stair,score=[],[0]*n
for _ in range(n):
    stair.append(int(input()))
if n<=2:
    print(sum(stair))
else:
    
    score[0]=stair[0]
    score[1]=stair[0]+stair[1]
    score[2]=max(stair[1]+stair[2],stair[0]+stair[2])
    for i in range(3,n):
        score[i]=max(score[i-3]+stair[i-1]+stair[i],score[i-2]+stair[i])
    print(score[-1])
