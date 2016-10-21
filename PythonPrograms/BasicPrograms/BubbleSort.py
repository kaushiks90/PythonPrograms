list = [1,8,4,3,5]
def BubbleSort(inputArray):
    for x in range(0,len(inputArray)):
        swapped=False
        for y in range(0,len(inputArray)-1):
            if inputArray[y] > inputArray[y+1]:
                (inputArray[y+1],inputArray[y]) = (inputArray[y],inputArray[y+1])
                swapped=True
        if swapped==False:
            break
    for z in range(0,len(inputArray)):
        print(inputArray[z])
BubbleSort(list)

