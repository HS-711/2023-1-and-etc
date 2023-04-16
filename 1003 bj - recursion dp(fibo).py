def fib_recursion(n):
    global cnt1,cnt0
    if n>1:
        return fib_recursion(n-2),fib_recursion(n-1)
    elif n==1:
        cnt1+=1
    elif n==0:
        cnt0+=1
    return True

def fib_reputation(n):
    global number
    number[0] = [1,0]
    number[1] = [0,1]
    if n >= 2:
        for i in range(2,n+1):
            a = number[i-1][0] + number[i-2][0]
            b = number[i-1][1] + number[i-2][1]
            number[i] = [a,b]
    return number[n]


t=int(input())
n=[]
for _ in range(t):
    n.append(int(input()))
for x in n:
    cnt1,cnt0=0,0
    number=[[0,0]]*(x+1)
    fib_recursion(x)
    print(cnt0,cnt1)
    answ=fib_reputation(x)
    print(answ[0],answ[1])
