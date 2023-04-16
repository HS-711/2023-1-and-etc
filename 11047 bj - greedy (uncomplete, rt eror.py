'''
n,k=list(map(int,input().split()))
a=[]
cnt=0
for _ in range(n):
    a.append(int(input()))
for x in range(n):
    if a[x]>k:
        b=a[:x]
b.sort(reverse=True)
for x in b:
    cnt+=k//x
    k=k%x
print(cnt)
'''
