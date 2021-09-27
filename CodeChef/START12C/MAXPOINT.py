# cook your dish here
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    x,y,z = map(int,input().split())
    res = 0
    for i in range(21):
        for j in range(21):
            for k in range(21):
                if (i*a)+(j*b)+(k*c) <=240:
                    res = max(res,(i*x)+(j*y)+(k*z))
    print(res)