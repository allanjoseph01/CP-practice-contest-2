n,q=map(int,input().split())
lst=[]
isprime=[]
for i in range(0,n+1):
    isprime.append(1)
for j in range(2,n+1):
    if isprime[j]==1:
        k=j*j
        while k<=n:
            isprime[k]=0
            k+=j
for m in range(2,n+1):
    if isprime[m]==1:
        lst.append(m)
def Noldprime(x):
    if x<13:
        return False
    for h in range(0,len(lst)-1):
        if (lst[h]+lst[h+1]+1)==x:
            return True
    return False
count=0
for t in lst:
    if Noldprime(t):
        count+=1
if count>=q:
    print("YES")
else:
    print("NO")
