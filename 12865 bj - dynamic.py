n,k=map(int,input().split())
weight,value=[0],[0]
for _ in range(n):
    w,v=list(map(int,input().split()))
    weight.append(w)
    value.append(v)
arr=[[0 for _ in range(k+1)] for _ in range(n+1)]
print(arr)
print(weight)
for row in range(1,n+1):
    for col in range(1,k+1):
        if weight[row]>col:
            arr[row][col]=arr[row-1][col]
        else:
            value1=value[row]+arr[row-1][col-weight[row]]
            value2=arr[row-1][col]
            arr[row][col]=max(value1,value2)
print(arr[n][k])
