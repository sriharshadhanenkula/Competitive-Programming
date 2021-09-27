# cook your dish here
for _ in range(int(input())):
    l = list(int(i) for i in input().split())
    c1 = l.count(1)
    c0 = l.count(0)
    if c1> c0:
        print("YES")
    else:
        print("NO")