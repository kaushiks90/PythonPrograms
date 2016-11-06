#Given an Array on N numbers partition the array based on the given number
#such that the elements lesser to that are in the left and elements greater are in the right
#Arr[9,2,3,8,5,6,7]  element given is 7 then the output should be
#[2,3,5,6,7,8,9]


listArray=[9,2,3,8,5,6,7]
def Partition(inputArray,start,end):
    x=inputArray[end]
    i=start-1
    for j in range(start,end):
        if(inputArray[j]<x):
            i=i+1
            (inputArray[i],inputArray[j])=(inputArray[j],inputArray[i])
    i=i+1
    temp=inputArray[i]
    inputArray[i]=x
    inputArray[end]=temp
    print(inputArray)
Partition(listArray,0,len(listArray)-1)
        


