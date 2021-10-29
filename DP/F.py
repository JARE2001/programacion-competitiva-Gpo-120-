tests= int(input())

while(tests):
    temp = input().split()
    n = int(temp[0])
    m = int(temp[1])
    a=0


    temp = input().split()
    
    for i in range(n):
        val = int(temp[i])
        if(val != i+1):
            a=i+1
    p = 0

    while m:
        temp = input().split()
        ri = float(temp[0])
        pi = float(temp[1])

        if(ri>=a):
            p += (1-p)*pi
        m-=1
    if a==0:
        p=1
    print(round(p,6))
    tests-=1
