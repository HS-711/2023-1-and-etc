n=int(input())
cnt=0
if n<100:
    print(n)
else:
    for x in range(1,n+1):
        n=len(str(x))
        han=str(x)
        flag=True
        if n<3:
            cnt+=1
        else:
            d=int(han[1])-int(han[0])
            for i in range(1,n):
                if not (int(han[i])-int(han[i-1]))==d:
                    flag=False
            if flag:
                cnt+=1
    print(cnt)
