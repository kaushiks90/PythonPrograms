#Rearrange the array in ZigZag Way
def Rearrange(inputArray):
    isless=True
    for i in range (0,len(inputArray)-1):
        if isless:
            if(inputArray[i]>inputArray[i+1]):
                (inputArray[i],inputArray[i+1])=(inputArray[i+1],inputArray[i])
        else:
            if(inputArray[i]<inputArray[i+1]):
               (inputArray[i],inputArray[i+1])=(inputArray[i+1],inputArray[i])
        isless=not isless       
    return inputArray
input = [4, 3, 2, 6, 7, 1, 9]
Rearrange(input)
print(input)

