def binary(start,end,target):
    if target>=99:
        return -1
    while start<=end:
        mid=(start+end)//2
        win_rate=100*(y+mid)//(x+mid)
        if win_rate>target:
            answ=mid
            end=mid-1
        elif win_rate<=target:
            start=mid+1
        else:
            break
    return answ
global x,y,answ
answ=0
x,y=list(map(int,input().split()))
print(binary(1,x,(100*y//x)))
