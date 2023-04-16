n,x=list(map(int,input().split()))
v=list(map(int,input().split()))
flag=True
while flag:
    for i in range(n):
        if v[i]>=x:
            x+=1
        else:
            result=i
            flag=False
            break
print(result+1)
