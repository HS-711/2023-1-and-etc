n,m,k=list(map(int,input().split()))
d=list(map(int,input().split()))
r_answ=''
start=0
end=n
while start<=end:
    mid=(start+end)//2
    prev=0
    answ='1'
    select=1
    for i in range(1,k):
        if d[i]-d[prev]>=mid:
            answ+='1'
            select+=1
            prev=i
            if select==m:
                break
        else:
            answ+='0'
    while len(answ)<k:
        answ+='0'
    if select==m:
        start=mid+1
        r_answ=answ
    else:
        end=mid-1
print(r_answ)
