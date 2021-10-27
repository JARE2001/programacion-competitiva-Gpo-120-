#k is the final hour were we want to know the position of the cat

def catPosition(spots, k):
    #if even cats will never cross
    if( spots%2 == 0):
       return (k%spots)+1
    else:
        return (((k//(spots//2))+k)%spots)+1


tests= int(input())
for test in range(tests):
    temp = input().split()
    print(catPosition(int(temp[0]),int(temp[1])-1))