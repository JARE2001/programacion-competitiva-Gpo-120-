

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)


def findXY(a,b,c):
    x,y = 1*(10**(a-1)),1*(10**(b-1))
  
   
    currGCD= gcd(x,y)
    while len(str(currGCD))!= c:
        if(len(str(currGCD))<c):
            pass
        if(len(str(currGCD))>c):
            a

    
    

digits =[0,1,2,3,4,5,6,7,8,9]
findXY(2,3,1)