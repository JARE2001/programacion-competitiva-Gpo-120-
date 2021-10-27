#Jorge Alan Ramirez Elias
def canSproduceT(s,t):
    n = len(s)
    m = len(t)

    if(m == 0):
        return "YES"
    if(n<m):
        return "NO"
    i=n-1
    j=m-1
    
    while(i>=0 and j>=0): 
        if s[i] == t[j]:
            i-=1
            j-=1
        else:
            i-=2
    if j == -1:
        return "YES"
    return "NO"

tests = int(input())
results=[]

while(tests):
    s = input()
    t = input()
    print(canSproduceT(s,t))
    tests-=1
