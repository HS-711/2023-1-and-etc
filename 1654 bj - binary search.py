def binary_search(left,right,target):
    answ=0
    while left<=right:
        lan=0
        mid=(left+right)//2
        #print(left,mid,right)
        for x in a:
            lan+=x//mid
        if lan>=target:
            answ=mid
            left=mid+1
        elif lan<target:
            right=mid-1
    return answ
k,n=list(map(int,input().split()))
global a
a=[]
for _ in range(k):
    a.append(int(input()))
print(binary_search(1,max(a),n))
