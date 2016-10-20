list=[3,4,1,2,78]
def ReverseArr(inputArray):
    for x in range(len(inputArray),0,-1):
        print(inputArray[x-1])
ReverseArr(list)
