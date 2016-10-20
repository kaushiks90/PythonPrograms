list = [1,2,3,4,1,2,4,3,2]
def BruteForceOdd(inputArray):
    for x in range(0,len(inputArray)):
        count = 0
        for y in range(1,len(inputArray)):
            if inputArray[x] == inputArray[y]:
                count = count + 1
    if count % 2 == 1:
        print(inputArray[x],"Occurs odd number of times")
BruteForceOdd(list)

