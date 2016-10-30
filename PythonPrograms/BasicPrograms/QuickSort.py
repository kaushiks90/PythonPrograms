def QuickSort(inputArray,start,length):
    if(start<length):
       q= Partition(inputArray,start,length-1)
       QuickSort(inputArray,start,q)
       QuickSort(inputArray,q+1,length-1)

def Partition(inputArray,start,length):
    x=inputArray[length]
    i=start-1;
    for j in range(start,length):
        if(inputArray[j]<x):
            i=i+1;
            (inputArray[j],inputArray[i])=(inputArray[i],inputArray[j])
    i=i+1
    temp=inputArray[i]
    inputArray[i]=x
    inputArray[length]=temp;
    return i

list = [9,7,3,8,5,6,10]
QuickSort(list,0,len(list))
for x in range(0,len(list)):
        print(list[x])



