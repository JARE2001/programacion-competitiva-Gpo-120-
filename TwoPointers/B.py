import math
def frogs(w,l,stones):
    acc =0
    
    for i in range(l):
        acc+=stones[i]
    accMin = acc
    for i in range(l,w-1):
        acc = acc - stones[i-l] + stones[i]
        accMin = min(acc,accMin)
    return accMin


temp = input().split()

w = int(temp[0])
l = int(temp[1])
temp = input().split()
stones=[]
for stone in temp:
    stones.append(int(stone))

print(frogs(w,l,stones))