# cook your dish here
for _ in range(int(input())):
    n = int(input())
    
    
    num = str(1)+(str(0)*(n-1))
    ran = str(9)+(str(9)*(n-1))
    
    for i in range(int(num),int(ran)):
        if i%2 != 0 and i%3 == 0 and i%9 !=0:
            print(i)
            break