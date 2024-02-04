n=int(input())
lst=[]
def isprime(y):
    if y<2:
        return False
    count=0
    for j in range(2,y):
        if y%j==0:
            return False
    return True
def firstprime(x):
    for i in range(2,x+1):
        if x%i==0 and isprime(i):
            return i
while n!=1:
    a=firstprime(n)
    n=n//a
    lst.append(a)
if len(lst)==1:
    print(lst[0])
else:
    for l in range(0,len(lst)-1):
        print(lst[l],end="*")
    print(lst[-1])
