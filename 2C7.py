n=int(input())
lst=[]
isprime=[]
for i in range(0,n+2):
    isprime.append(1)
for j in range(2,n+2):
    if isprime[j]==1:
        k=j*j
        while k<=n+1:
            isprime[k]=0
            k+=j
for m in range(2,n+2):
    if isprime[m]==1:
        lst.append(m)
ans1=[]
count=1
ans=[]
for t in range(0,n+2):
    ans1.append(1)
for r in range(2,n+2):
    if ans1[r]==1 and r in lst:
        u=r*r
        while u<=n+1:
            ans1[u]=count+1
            u+=r
        if u!=r*r:
            count+=1
for o in range(2,n+2):
    ans.append(ans1[o])
print(count)
for s in ans:
    print(s,end=" ")
    

    
