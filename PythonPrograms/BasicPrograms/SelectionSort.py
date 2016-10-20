def SelectionSort(inputArray):
    for x in range(0,len(inputArray)):
        changeArray=inputArray[x]
        for y in range(x+1,len(inputArray)):
            if inputArray[x]>inputArray[y]:
                (inputArray[x],inputArray[y])=(inputArray[y],inputArray[x])
    for x in range(0,len(inputArray)):
        print(inputArray[x])
list=[7,5,1,2,3]
SelectionSort(list)



