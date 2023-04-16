def long_check(arr):
    if len(arr)==4:
        arr.remove(min(arr))
        temp=min(arr)
        arr=[]
        arr.append(temp)
    return arr

def div(n,arr):
    global answ,cnt,result
    if n!=2:
        n=n//2
        temp=[]
        for i in range(n):
            temp.append(arr[i][:n])
        div(n,temp)
        temp=[]
        for i in range(n):
            temp.append(arr[i][n:])
        div(n,temp)
        temp=[]
        for i in range(n,2*n):
            temp.append(arr[i][:n])
        div(n,temp)
        temp=[]
        for i in range(n,2*n):
            temp.append(arr[i][n:])
        div(n,temp)
        
    else:
        k=[]
        for x in arr:
            for y in x:
                k.append(y)
        k.remove(min(k))
        answ.append(min(k))
        cnt+=1
    if cnt==4:
        answ.remove(min(answ))
        result.append(min(answ))
        cnt=0
        answ=[]
        result=long_check(result)
    return result
    
cnt=0       
answ,result,a=[],[],[]
n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
if n==1:
    print(arr[0])
elif n==2:
    for x in arr:
        for y in x:
            a.append(y)
    a.remove(min(k))
    print(min(k))
else:
    main=div(n,arr)
    print(main[0])
