n=int(input())
l=list(map(int,input().split()))
m=int(max(l)**0.5)+1
lst=[]
isprime=[]
for i in range(0,m+1):
    isprime.append(1)
for j in range(2,m+1):
    if isprime[j]==1:
        k=j*j
        while k<=m:
            isprime[k]=0
            k+=j
for x in range(2,m+1):
    if isprime[x]==1:
        lst.append(x)
count=0
for t in l:
    sq=int(t**0.5)
    ma=sq*sq
    if ma==t:
        if sq in lst:
            print("YES")
    else:
        print("NO")
