def InsertionSort(inputArray):
    for x in range(1,len(inputArray)):
        key = inputArray[x]
        y = x - 1
        while(y >= 0 and inputArray[y] > key):
            inputArray[y + 1] = inputArray[y]
            y = y - 1
        inputArray[y + 1] = key
    for x in range(0,len(inputArray)):
        print(inputArray[x])
list = [7,5,1,2,3]
InsertionSort(list)

