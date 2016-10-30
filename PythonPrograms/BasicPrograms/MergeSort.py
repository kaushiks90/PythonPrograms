def MergeSort(inputArray):
    if(len(inputArray)<2):
        return
    mid=len(inputArray)//2
    left=[]
    left=inputArray[0:mid]
    right=[]
    right=inputArray[mid:len(inputArray)]
    MergeSort(left)
    MergeSort(right)
    SortAndMerge(left,right,inputArray)
    
def SortAndMerge(left,right,inputArray):
    lc=len(left)
    rc=len(right)
    i=0
    j=0
    k=0
    while(i<lc and j<rc):
        if(left[i]<right[j]):
            inputArray[k]=left[i]
            i=i+1
        else:
            inputArray[k]=right[j]
            j=j+1
        k=k+1
    while(i<lc):
        inputArray[k]=left[i]
        i=i+1
        k=k+1
    while(j<rc):
        inputArray[k]=right[j]
        j=j+1
        k=k+1


list = [7,5,1,2,3,8]
MergeSort(list)

for x in range(0,len(list)):
        print(list[x])



