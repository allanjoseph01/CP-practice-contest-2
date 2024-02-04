n=int(input())
lst=list(map(int,input().split()))
a=max(lst)
b=min(lst)
count=0
mai=lst.index(a)
while mai!=0:
    lst[mai-1],lst[mai]=lst[mai],lst[mai-1]
    count+=1
    mai-=1
mii=len(lst) - 1 - lst[::-1].index(b)
p=len(lst)-1
d=p-mii
count=count+d
print(count)
