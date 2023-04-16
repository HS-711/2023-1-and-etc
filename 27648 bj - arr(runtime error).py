n,m,k=list(map(int,input().split()))
arr=[[1 for _ in range(m)] for _ in range(n)]
cnt=0
while cnt<k:
    for row in range(0,n):
        for col in range(0,m):
            if row==n-1 and col==m-1:
                cnt+=1
            else:
                if col==m-1:
                    if not arr[row][col]<arr[row+1][col]:
                        arr[row+1][col]+=1
                elif row==n-1:
                    if not arr[row][col]<arr[row][col+1]:
                        arr[row][col+1]+=1
                else:
                    if not arr[row][col]<arr[row+1][col]:
                        arr[row+1][col]+=1
                    if not arr[row][col]<arr[row][col+1]:
                        arr[row][col+1]+=1

flag=True
while flag:
    for i in range(n):
        for j in range(m):
            if arr[i][j]>k:
                flag=False

    if flag:
        for i in range(n):
            for j in range(m):
                if j!=m-1:
                    print(arr[i][j],end=' ')
                else:
                    print(arr[i][j])
        flag=False
    else:   
        print('NO')
