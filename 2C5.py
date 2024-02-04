n=int(input())
lst=list(map(int,input().split()))
maxl=lst[0]
minl=lst[0]
count=0
for i in range(1,n):
    if lst[i]<minl:
        minl=lst[i]
        count+=1
    if lst[i]>maxl:
        maxl=lst[i]
        count+=1
print(count)
    
