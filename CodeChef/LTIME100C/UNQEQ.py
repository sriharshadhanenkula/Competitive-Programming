# cook your dish here
for _ in range(int(input())):
    n = int(input())
    
    if n%2 == 0:
        x = int(n/2) 
        if x%2 ==0:
            l = list(int(i) for i in range(1,n+1))
            l1 = l[0:n//4]+l[n-(n//4):]
            l2 = l[(n//4): n-(n//4)]
            print("YES")
            print(*l1)
            print(*l2)
        else:
            print("NO")
    else:
        print("NO")
        
    