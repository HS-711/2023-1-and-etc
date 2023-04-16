def binary_search(start,end,target):
    if end==target:
        return end
    while start<end:
        mid=(start+end)//2
        cnt=0
        for i in range(1,n+1):
            cnt+=min(n,mid//i)
        if cnt>=target:
            end=mid
        else:
            start=mid+1
    return mid

n=int(input())
k=int(input())
print(binary_search(1,n**2,k))
