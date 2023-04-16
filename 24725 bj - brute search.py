cnt=0
mbti=''
row,col=list(map(int,input().split()))
arr=[['a' for _ in range(col+2)]for _ in range(row+2)]
for x in range(1,row+1):
    k=input()
    for i in range(col):
        arr[x][i+1]=k[i]
for row in range(1,row+1):
    for col in range(1,col+1):
        idx=[]
        if arr[row][col]=='I' or arr[row][col]=='E':
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if arr[row+i][col+j]=='N' or arr[row+i][col+j]=='S':
                        idx.append([i,j])
            if idx!=[]:
                for x in idx:
                    if arr[row+2*x[0]][col+2*x[1]]=='F' or arr[row+2*x[0]][col+2*x[1]]=='T':
                        if arr[row+3*x[0]][col+3*x[1]]=='P' or arr[row+3*x[0]][col+3*x[1]]=='J':
                            cnt+=1
print(cnt)
