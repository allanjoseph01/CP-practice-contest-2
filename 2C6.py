n=int(input())
sum1=0
max1=0
for _ in range(0,n):
    a_,b_=map(int,input().split())
    sum1+=(b_-a_)
    if sum1>max1:
        max1=sum1
print(max1)
