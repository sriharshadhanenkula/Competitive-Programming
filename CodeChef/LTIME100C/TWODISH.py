# cook your dish here
for _ in range(int(input())):
    n,a,b,c = map(int,input().split())
    
    if a+c <= b and a+c >=n:
        print("YES")
    elif a+c >b and b >= n:
        print("YES")
    else:
        print("NO")