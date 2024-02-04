n,m=map(int,input().split())
l=[]
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
for q in range(2,n+1):
    if isprime[q]==1:
        lst.append(q)
for w in range(0,n):
    l.append(0)
for o in range(0,m):
    s,t=map(str,input().split())
    ith=int(t)
    if s=="+":
        if o==0:
            print("Success")
        else:
            if ith in lst:
                if l[ith-1]==0:
                    l[ith-1]=1
                    print("Success")
                else:
                    print("Already on")
            else:
                for t in lst:
                    if ith%t==0:
                        z=1
                        while t*z<n:
                            if l[(t*z)-1]==1:
                                print("Conflict with ",t*z)
                                break
                            else:
                                z+=1
    if s=="-":
        if l[ith-1]==1:
            l[ith-1]=0
            print("Success")
        else:
            print("Already off")
            	
