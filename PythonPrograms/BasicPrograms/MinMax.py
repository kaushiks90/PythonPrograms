#MinMax 
#given an Array find the min element and max element 
#[10,5,6,9,1,64] Min element=1 and Max elemet =64
#We will see 2 methods to find the solutin iterative and Recursive
listArray=[10,5,6,9,1,64]
def MinMaxIterative(inputArray):
    min=max=inputArray[0]
    for x in range(1,len(inputArray)):
        if(inputArray[x]<min):
            min=inputArray[x]
        elif(inputArray[x]>max):
            max=inputArray[x]

    print("Minimum,Maximum",min,max)

MinMaxIterative(listArray)

min=9999
max=0
def getMaximum(a, b):
    if b > a:
        return b
    else:
        return a
    
def getMinimum(a, b):
    if b < a:
        return b
    else:
        return a

def MinMaxRecursion(inputArray,start,end):
    global min
    global max
    if(end-start>2):
        mid=(start+end)//2
        MinMaxRecursion(inputArray,start,mid)
        MinMaxRecursion(inputArray,mid,end)
    else:
        inputArray=inputArray[start:end]
        if end-start==1:
            inputArray.append(inputArray[0])
        min=getMinimum(min,getMinimum(inputArray[0],inputArray[1]))
        max=getMaximum(max,getMaximum(inputArray[0],inputArray[1]))
    

listArray=[10,5,6,9,1,64]
MinMaxRecursion(listArray,0,len(listArray))
print("Minimum,Maximum",min,max)



