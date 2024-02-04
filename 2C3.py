n=int(input())
if n%2!=0:
    print("-1")
else:
    lst=[]
    for i in range(1,n+1):
        lst.append(i)
    j=0
    while j<len(lst):
        lst[j],lst[j+1]=lst[j+1],lst[j]
        j+=2
    for k in lst:
        print(k,end=" ")
