#jorge alan ramirez A01701350
def findXY(a,b,c):
    g=10**(c-1)
    
    x,y =g,g

    nA =10**(a-1)
    nB =10**(b-1)

    while(x<nA):
        x*=2
    while(y<nB):
        y*=3
    print(x,y)
  
tests = int(input())
while tests:
    temp = input().split()
    findXY(int(temp[0]),int(temp[1]),int(temp[2]))
    tests-=1