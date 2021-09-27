# cook your dish here

    
for _ in range(int(input())):
    c = 0 
    l,r = map(int,input().split())
    if (l % 3 == 0):
        print (((r // 3) - ( l// 3)) + 1)
    else:
        print((r // 3) - (l // 3))