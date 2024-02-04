n=int(input())
for y in range(0,n):
    a,b=map(int,input().split())
    if a%2==0 and b%2==0:
        print("YES")
    elif a%2!=0 and b%2!=0:
        print("YES")
    else:
        if a-b>2:
            print("YES")
        else:
            print("NO")
                
            
        
