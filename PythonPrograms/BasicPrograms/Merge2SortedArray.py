#Given 2 Sorted Array
#[1,9,10,15] [2,13,78,90]
#Arrange it to [1,2,9,10,13,15,78,90]
i=0
j=0
k=0
    
def Merge2SortedArrays(arr1,arr2):
    lc=len(arr1)
    lr=len(arr2)
    result=[0 for x in range(0,lc+lr)]
    global j
    global i
    global k
    while(i<lc and j<lr):
        if(arr1[i]<arr2[j]):
            result[k]=arr1[i]
            i=i+1
        elif(arr2[j]<arr1[i]):
            result[k]=arr2[j]
            j=j+1
        k=k+1;
    while(i<lc):
        result[k]=arr1[i]
        k=k+1
        i=i+1
    while(j<lr):
        result[k]=arr2[j]
        k=k+1
        j=j+1

    print(result)

arr1=[1,9,10,15] 
arr2=[2,13,78,90]
Merge2SortedArrays(arr1,arr2)
