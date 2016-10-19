list = [3,4,1,1,2]
def BruteForceTech(inputArray):
    for x in range(1,len(inputArray)):
        count = 0
        for y in range(0,len(inputArray)):
            if x == inputArray[y]:
                count = count + 1
        print(x," occurs ",count," times")
BruteForceTech(list)
#Optimized Solution

print("Optimized Solution")
def OptimizedTechnique(inputArray):
    n=len(inputArray)-1
    for x in range(0,len(inputArray)):
        inputArray[x]=inputArray[x]-1
    
    for x in range(0,len(inputArray)):
        res=0
        res=(inputArray[x]%(len(inputArray)-1))
        inputArray[res]=inputArray[res]+n

    
    for x in range(0,len(inputArray)):
       res=(inputArray[x])//(len(inputArray)-1)
       print(x+1," ",res)
       inputArray[x]=(inputArray[x]%(len(inputArray)-1))+1


OptimizedTechnique(list)