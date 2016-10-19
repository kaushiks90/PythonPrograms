List=[98,23,54,12,20,7,27]
def FindLeadersInArray(inputArray):
    currentLeader=0
    for x in range(len(inputArray),0,-1):
        if inputArray[x-1]>currentLeader:
            currentLeader=inputArray[x-1]
            print(currentLeader)
FindLeadersInArray(List)

