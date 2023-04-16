n=int(input())
rank=[0 for _ in range(n)]
predict=[0 for _ in range(n)]
unhappy=0
for i in range(n):
    predict[i]=int(input())
for x in range(n):
    if rank[predict[x]-1]==0:
        rank[predict[x]-1]=predict[x]
    else:
        fore,back=1,1
        flag=True
        while flag:
            if not predict[x]+back>n:
                if rank[predict[x]-1+back]==0:
                    rank[predict[x]-1+back]=predict[x]
                    unhappy+=back
                    flag=False
                else:
                    back+=1
            elif not predict[x]-fore<1:
                if rank[predict[x]-1-fore]==0:
                    rank[predict[x]-1-fore]=predict[x]
                    unhappy+=fore
                    flag=False
                else:
                    fore+=1
print(unhappy)
